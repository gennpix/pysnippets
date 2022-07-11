# coding: utf8

import random
from multiprocessing import Pool, shared_memory


def worker(i, shared_var):
    shared_var[0] += 1
    result = random.randint(1, 100)
    print(f"{shared_var[0]}/{shared_var[1]} arg: {i} result: {result}")
    return result


def main():
    shared_var = shared_memory.ShareableList([0, 100])
    pool = Pool(8)
    workers = [pool.apply_async(func=worker, args=(i, shared_var)) for i in range(10)]
    pool.close()
    pool.join()

    result = []
    for res in workers:
        r = res.get()
        if not r:
            continue

        result.append(r)

    print(f"result: {result}")


if __name__ == '__main__':
    main()
