from typing import List

import numpy as np
import itertools


def is_sum_k(n: int, arr: List[int], k: int) -> bool:
    for i in range(1, n + 1):
        cmb = list(itertools.combinations(arr, i))
        for j in range(len(cmb)):
            if np.array(cmb[j]).sum() == k:
                print(np.array(cmb[j]))
                return True
    return False


def case1():
    return is_sum_k(n=4, arr=[1, 2, 4, 7], k=13)


def case2():
    return is_sum_k(n=4, arr=[1, 2, 4, 7], k=15)


if __name__ == '__main__':
    print(case1())
    print(case2())
