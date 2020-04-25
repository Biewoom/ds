import os
import sys

sys.path.append("C:\\Users\\likemin\\OneDrive\\바탕 화면\\Algo test\\DS")
from Sets import Disjoint_set as ds
from RandomGenerater import make_randomString, make_tuple, make_int

Operater1 = ['make', 'block']
Operater2 = ['delete', 'liberate', 'showFriends', 'showBlocks']

def Disjoint_Test(llist):
    global Operater1, Operater2
    myds = ds.DisjointSet()

    for elem in llist:
        op, info = elem
        print("operater: ", elem)
        if op == 'make': myds.make_connection(info)
        elif op == 'block': myds.block(info)
        elif op == 'delete': myds.delete(info)
        elif op == 'showFriends': print( myds.show_myfriends(info) )
        elif op == 'showGroup': print( myds.show_groupsize(info) )
        elif op == 'showBlocks': print( myds.show_blocks(info) )
        elif op == 'liberate': myds.liberate(info)
        else: print("Impossible")

    myds.showAll()
    #random pick
    r = myds.rootSet.copy().pop()
    print("%d's blocks: "%(r.id), myds.show_blocks(r.id))
    print("%d's friends: "%(r.id), myds.show_myfriends(r.id))
    print("%d's Total members: "%(r.id), myds.show_groupsize(r.id))



if __name__ == '__main__':
    n, s, e = map(int, input().split())
    ops = make_randomString(n, Operater1+Operater2)
    llist = []
    for op in ops:
        if op in Operater1:
            llist.append((op, make_tuple(s, e)))
        else:
            llist.append((op, make_int(s, e) ) )
    Disjoint_Test(llist)
