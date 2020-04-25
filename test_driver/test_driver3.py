import os
import sys
import random

sys.path.append("C:\\Users\\likemin\\OneDrive\\바탕 화면\\Algo test\\DS\\")

from LinearDs import DynamicArray as dyarr
from RandomGenerater import make_tuple, make_int, make_randomString, make_random_call, make_slice, make_randomlist

operater1 = ['append', 'in', 'count', 'pop']# one argument
operater2 = ['get'] # slice, tuple, int
operater3 = ['set'] # slice-list and tuple and list and int-int
operater4 = ['make', 'extend'] # no need argument

def dyarr_test(llist):
    arr_container = []; initial_size = 10
    cur_arr = dyarr.DynamicArray(10)
    # TEST: append
    for elem in llist:
        print("query: ", elem)
        op, info = elem
        if op == 'append': cur_arr.append(info)
        elif op == 'in': print('%d is in arr: '%info, info in cur_arr)
        elif op == 'get': print("get: ", cur_arr[info] )
        elif op == 'count': print("Count %d"%info, cur_arr.count(info))
        elif op == 'pop' or op == 'pop2': cur_arr.pop(info)
        elif op == 'set':
            index, v = info; cur_arr[index] = v
        elif op == 'make':
            arr_container.append(cur_arr); cur_arr = dyarr.DynamicArray(10)
        elif op == 'extend':
            while arr_container:
                cur_arr.extend(arr_container.pop(0))

    # finally
    print("SET TEST: ")
    print("In container")
    while arr_container:
        cur_arr.extend(arr_container.pop(0))
    print("EXTEND ALL: ", len(cur_arr))
    cur_arr[::] = 5
    print("Set by slicing: ", cur_arr)

if __name__ == '__main__':
    n, s, e = map(int , input().split() )
    ops = make_randomString(n, operater1+operater2 + operater3 + operater4)
    func_list = [make_int, make_tuple, make_slice]
    llist = []
    for op in ops:
        if op in operater1:
            llist.append((op,make_int(s, e)))
        elif op in operater2:
            llist.append((op, make_random_call(func_list,s, e)))
        elif op in operater3:
            llist.append((op, (make_randomlist(5, s, e), make_randomlist(5, s, e))))
        else:
            llist.append((op, None))

    dyarr_test(llist)
