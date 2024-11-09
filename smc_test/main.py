from typing import List, Tuple
from mpyc.runtime import mpc

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

    client_data: List[List[Tuple[int, float]]] = [
        [(1, 0.8), (1, 0.3)],  # Client 1's data
        [(1, 0.5), (1, 0.0)],  # Client 2's data
        [(1, 0.8), (1, 0.1)],  # Client 3's data
        # [(1, 30), (1, 25)],  # Client 3's data
    ]

    await mpc.start()
    # dont do list of lists to make sending input easier (maybe change)
    id = lambda idx: secnum(mpc.pid * 100 + idx)
    myinput = [
        [id(idx), secnum(it[0]), secnum(int(it[1] * 10))]
        for idx, it in enumerate(client_data[mpc.pid])
    ]
    inputs = mpc.input(flatten(myinput), senders=peers)

    union = aggregate(flatten(inputs), 3)
    sorted_union = await sort(union, k=2)

    unique_tags = [entry[0] for entry in sorted_union]  # Extract only unique tags
    revealed_tags = await mpc.output(unique_tags)
    # out = await mpc.output(flatten(sorted_union))
    # p_out = aggregate(out, 3)
    # my_positions = [i for i, tag in enumerate(revealed_tags) if tag // 100 == mpc.pid]

    # for idx, it in enumerate(client_data[mpc.pid]):
    #     pos = revealed_tags.index(id(idx))
    #     print(it, revealed_tags[pos])

    my_positions = []
    for i, tag in enumerate(revealed_tags):
        if tag // 100 == mpc.pid:
            client_idx = tag - (mpc.pid * 100)
            print(i, client_data[mpc.pid][client_idx])

    # Output sorted positions with associated input data for the current party
    print(f"Party {mpc.pid} sorted positions and associated data: {my_positions}")
    #
    global_sort = sorted(flatten(client_data), key=lambda it: it[1])
    for idx, g in enumerate(global_sort):
        print(f"{idx}: {g}")
    print("global view", global_sort)

    await mpc.shutdown()


if __name__ == "__main__":
    mpc.run(main())
