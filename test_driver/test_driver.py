import os
import sys

from RandomGenerater import make_radomlist
from Heaps import BinomialHeap
from LinearDs import DoubleLinkedList
from Tree import BST_node as b
# from Fibonacciheap
#
def BSTnode_test(llist):
    bst = b.BST()
    #insort
    for elem in llist:
        bst.insort(elem)
    #print
    print("bst after insort: ", bst)
    print("Inorder traversal: ", bst.inorder_trav())
    # print("Rorder traversal: ", bst.reverse_trave())
    # print("preOrder traversal: ", bst.preorder_trav())
    # print("postOrder traversal: ", bst.postorder_trav())
    # print("bfs traversal: ", bst.bfs_trav())
    # look up #
    print("Find 5<left>: ", bst.bisect_left(5))
    print("Find 5<right>: ", bst.bisect_right(5))
    print("Find 1000<left>: ", bst.bisect_left(1000))
    print("Find 1000<right>: ", bst.bisect_right(1000))
    # update #
    while bst.delete(5) > 0:
        print("bst after delete 5: ", bst.inorder_trav())
        print(bst)
    print(bst.update(4, 100))
    print(bst.update(4, 100))
    print(bst.update(4, 100))
    print('Update 5: ', bst.inorder_trav())
    print('bst after update: ', bst)
    # research #
    print("Find 5<left>: ", bst.bisect_left(5))
    print("Find 5<right>: ", bst.bisect_right(5))



def DoubleLinkedList_Test(llist):
    Dll = DoubleLinkedList()

    for elem in llist:
        Dll.appendleft(elem)
    print('appendleft Test<It will be reversed>: ', Dll)
    while len(Dll):
        Dll.popleft()

    for elem in llist:
        Dll.appendright(elem)
    print("appendright Test<It will be same>: ", Dll)

    # print("Popleft Test: ", Dll.popleft())
    # print("Dll with %d elems: "%(len(Dll)), Dll)
    # print('Popright Test: ', Dll.popright())
    # print("Dll with %d elems: "%(len(Dll)), Dll)

    # indexing Test #
    Dll[0] = 100000; Dll[5] = -1000000
    print("Indexing_test: ", Dll)
    print("Indexing_test: -3 ", Dll[-3])
    print("Indexing_test: -1", Dll[-1])
    print("In Test: ", 100000 in Dll)

def Binomial_Test(llist):

    BH = BinomialHeap()
    for elem in llist:
        BH.insert(elem)

    sorted_res = []
    while len(BH) > 0:
        sorted_res.append(BH.delete_min())

    print("sorted_res: ", sorted_res)

    # merge test #
def Binomial_MergeTest(ListOfList):

    if len(ListOfList) == 0: return "Impossible"
    BH1 = BinomialHeap()
    for elem in ListOfList[0]:
        BH1.insert(elem)

    for ll in ListOfList[1:]:
        temp_BH = BinomialHeap()
        for elem in ll:
            temp_BH.insert(elem)
        # merge
        BH1 = merge(BH1, temp_BH)

    sorted_res = []
    while len(BH1) > 0:
        sorted_res.append(BH1.delete_min())

    print("sorted_res: ", sorted_res)

if __name__ == '__main__':
    t = int(input())
    llist = []
    for iter_t in range(t):
        n, start, end = tuple( map(int, input().split()) )
        ll = make_radomlist(n, start, end)
        llist.append(ll)
        print("Input: ",ll)
        BSTnode_test(ll)
