import os
import re
import sys
import math
import random

#my definded
from RandomGenerater import make_radomlist

def go_down(arr, i):
    left_child = 2*(i+1) - 1; right_child = 2*(i+1);
    smallest = i

    if left_child < len(arr) and arr[left_child] < arr[smallest]: smallest = left_child;
    if right_child < len(arr) and arr[right_child] < arr[smallest]: smallest = right_child;

    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        go_down(arr, smallest)

def go_up(arr, i):
    parent = i//2

    if i > 0 and arr[i] < arr[parent]:
        arr[i], arr[parent] = arr[parent], arr[i]
        go_up(arr, parent)

def heappush(arr, v):
    arr.append(v); size = len(arr)
    new_pose = size - 1
    go_up(arr, new_pose)
    return

def heappop(arr):
    arr[0], arr[len(arr)-1] = arr[len(arr)-1], arr[0]
    output = arr.pop(-1)
    go_down(arr, 0)
    return output

def heapify(array):
    res = []
    for v in array:
        heappush(res, v)

    test_res = []
    while res:
        test_res.append(heappop(res))

    return test_res


if __name__ == "__main__":
    t = int( input() )

    for t_iter in range(t):
        n = int(input())
        array = make_radomlist(n, 1, 60)
        print("Input: ", array)
        result = heapify(array)
        print(*result)
