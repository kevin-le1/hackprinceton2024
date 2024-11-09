from collections import defaultdict
from typing import List, Tuple
from mpyc.runtime import mpc

type UUID = str


class PatientData:
    def __init__(self, t, r):
        self.r = r
        self.t = t

    def __lt__(self, other):
        primary_lt = mpc.lt(self.t, other.t)
        primary_equal = mpc.eq(self.t, other.t)

        secondary_lt = mpc.lt(self.r, other.r)

        return mpc.if_else(primary_equal, secondary_lt, primary_lt)


flatten = lambda it: [i for _ in it for i in _]
aggregate = lambda it, n=3: [it[i : i + n] for i in range(0, len(it), n)]


# type later
async def sort(*data):
    """Sort N lists of tuples (specialist: mpc.SecInt, risk_score: mpc.SecInt) by key k

    For our case, we convert the string specialist into an integer representation and then convert it
    to the mpc.SecInt. It shouldn't be considered in the sort, however.
    """
    together = [inner for outer in data for inner in outer]
    result = mpc.sorted(together, key=lambda it: PatientData(it[1], it[2]))
    return result


ht = {
    "Cardiologist": 1,
    "Orthopedic": 2,
}

lookup_key = lambda v, h: "".join([k1 for k1, v1 in h.items() if v1 == v])


async def main():
    secnum = mpc.SecInt(64)
    m = len(mpc.parties)
    peers = list(range(m))

    client_data: List[List[Tuple[int, str, int]]] = [
        [(1, "Cardiologist", 80), (2, "Orthopedic", 3)],
        [(1, "Orthopedic", 50), (2, "Cardiologist", 2)],
        [(1, "Orthopedic", 81), (2, "Cardiologist", 10)],
    ]

    await mpc.start()
    # dont do list of lists to make sending input easier (maybe change)
    id = lambda idx: secnum(mpc.pid * 100 + idx)
    # to_int = lambda s: int.from_bytes(s.encode(), "big")
    to_int = lambda s: ht.get(s, 0)
    serialize = lambda data: [
        [id(idx), secnum(to_int(it[1])), secnum(it[2])] for idx, it in enumerate(data)
    ]

    myinput = serialize(client_data[mpc.pid])
    inputs = mpc.input(flatten(myinput), senders=peers)
    # print(
    #     f"Node {mpc.pid} secure inputs:", aggregate(await mpc.output(flatten(inputs)))
    # )

    union = aggregate(flatten(inputs), 3)
    sorted_union = await sort(union)

    # keep commented in prod
    # res = await mpc.output(flatten(sorted_union))
    # print("res", aggregate(res, 3))

    unique_tags = [[entry[0], entry[1]] for entry in sorted_union]
    revealed_tags = await mpc.output(flatten(unique_tags))
    tag_specialist = aggregate(revealed_tags, 2)
    # print(tag_specialist)

    print("local view")
    c = 0
    prev = None
    res = defaultdict(list)
    # 0 indexed ranking
    for i, it in enumerate(tag_specialist):
        tag = it[0]
        type = it[1]
        specialist = lookup_key(type, ht)

        if type != prev:
            c = 0
        # print(i, tag)
        if tag // 100 == mpc.pid:
            client_idx = tag - (mpc.pid * 100)
            print(specialist)
            res[specialist].append((c, client_data[mpc.pid][client_idx][0]))
            print(c, client_data[mpc.pid][client_idx])
        prev = it[1]
        c += 1

    # remove global sort in final when move away from static input
    # global_sort = sorted(flatten(client_data), key=lambda it: (it[1], it[2]))
    # print("global view")
    # c = 0
    # prev = None
    # for g in global_sort:
    #     if prev != g[1]:
    #         c = 0
    #     print(f"{c}: {g}")
    #     c += 1
    #     prev = g[1]

    print(res)

    await mpc.shutdown()


if __name__ == "__main__":
    mpc.run(main())
