from dataclasses import dataclass
from typing import List, Tuple
from mpyc.runtime import mpc

type UUID = str


@dataclass
class PatientData:
    patient_id: UUID
    specialist_type: str
    risk_score: int  # [0-100]


flatten = lambda it: [i for _ in it for i in _]
aggregate = lambda it, n=3: [it[i : i + n] for i in range(0, len(it), n)]


# type later
async def sort(*data, k: int = 1):
    """Sort N lists of tuples (specialist: mpc.SecInt, risk_score: mpc.SecInt) by key k

    For our case, we convert the string specialist into an integer representation and then convert it
    to the mpc.SecInt. It shouldn't be considered in the sort, however.
    """
    together = [inner for outer in data for inner in outer]
    result = mpc.sorted(together, key=lambda it: it[k])
    return result


async def main():
    secnum = mpc.SecInt()
    m = len(mpc.parties)
    peers = list(range(m))

    client_data: List[List[Tuple[int, str, int]]] = [
        [(1, "Cardiologist", 80), (2, "Orthopedic", 3)],
        [(1, "Orthopedic", 50), (2, "Cardiologist", 2)],
        [(1, "Orthopedic", 80), (2, "Cardiologist", 10)],
    ]

    await mpc.start()
    # dont do list of lists to make sending input easier (maybe change)
    id = lambda idx: secnum(mpc.pid * 100 + idx)
    to_int = lambda s: int.from_bytes(s.encode(), "big")
    serialize = lambda data: [
        [id(idx), secnum(to_int(it[1])), secnum(it[2])] for idx, it in enumerate(data)
    ]

    myinput = serialize(client_data[mpc.pid])
    inputs = mpc.input(flatten(myinput), senders=peers)

    union = aggregate(flatten(inputs), 3)
    sorted_union = await sort(union, k=2)

    unique_tags = [entry[0] for entry in sorted_union]
    revealed_tags = await mpc.output(unique_tags)

    print("local view")
    for i, tag in enumerate(revealed_tags):
        if tag // 100 == mpc.pid:
            client_idx = tag - (mpc.pid * 100)
            print(i, client_data[mpc.pid][client_idx])

    # remove global sort in final when move away from static input
    global_sort = sorted(flatten(client_data), key=lambda it: it[2])
    print("global view")
    for idx, g in enumerate(global_sort):
        print(f"{idx}: {g}")

    await mpc.shutdown()


if __name__ == "__main__":
    mpc.run(main())
