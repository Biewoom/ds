import os
import sys

#my defined module

class BinomialTree:

    class BinomialNode:

        def __init__(self, data):
            self.data = data
            self.children = []

        def swap(self, other_node):
            self.data, other_node.data = other_node.data, self.data

    def __init__(self, data):
        new_node = self.BinomialNode(data)
        self.rank = 0
        self.next = None
        self.root = new_node

    def __len__(self):
        return pow(2, self.rank)

    def mergeTree(self, other_bt):
        self.rank += 1
        if self.peak() > other_bt.peak():
            self.root.swap(other_bt.root) #swap
            other_bt.heapify()
        other_bt.next = None
        self.root.children.append(other_bt)

    def get_children(self):
        return self.root.children

    def min_children(self):
        if len(self.get_children()) == 0: return sys.maxsize
        return min( [v.peak() for v in self.get_children()])

    def heapify(self):
        cur = self.root; child_Min = self.min_children()
        if self.peak() <= child_Min: return
        else:
            for subtree in self.get_children():
                if subtree.peak() == child_Min:
                    self.root.swap(subtree.root)
                    subtree.heapify()
                    break

    def peak(self):
        return self.root.data

class BinomialHeap:

    def __init__(self):
        self.head = None
        self.min = sys.maxsize
        self.biggestRank = 0
        self.size = 0

    def __str__(self):
        return self._str()

    def __len__(self):
        return self.size

    def _str(self):
        return 'Minimum is %d, big_rank: %d and size: %d'%(self.min, self.biggestRank, self.size)

    def _update(self):
        cur = self.head; self.min = sys.maxsize; self.biggestRank = -1; self.size = 0;
        while cur:
            self.min = min(self.min, cur.peak()); self.biggestRank = max(self.biggestRank, cur.rank); self.size += 1;
            cur = cur.next;
        return

    def push(self, new_bt, start_cur = None):
        # keep rank-sorted linked_list
        cur = start_cur if start_cur else self.head
        if not cur: self.head = new_bt; new_bt.next = None
        else:
            pre_cur = None
            while cur:
                if new_bt.rank == cur.rank:
                    ##### delete curent####
                    if pre_cur: pre_cur.next = cur.next
                    else: self.head = cur.next
                    #######################
                    cur.mergeTree(new_bt); new_bt = cur; new_bt.next = None
                    self.push(new_bt, pre_cur)
                    break
                elif new_bt.rank < cur.rank:
                    if pre_cur: pre_cur.next = new_bt
                    else: self.head = new_bt
                    new_bt.next = cur
                    break
                else: pre_cur = cur; cur = cur.next
            else:
                pre_cur.next = new_bt; new_bt.next = None
        self._update()

    def insert(self, data):
        NewBinomialTree = BinomialTree(data)
        self.push(NewBinomialTree)
        return

    def meld(self, other_bh):
        while len(other_bh):
            self.push(other_bh.pop())

    def delete_min(self):
        res = self.min; cur = self.head;
        # find peak
        pre_cur = None; target_bt = None;
        if self.size <= 0: raise ValueError('NO BT')
        while cur:
            if cur.peak() == self.min:
                # delete #
                target_bt = cur
                if pre_cur: pre_cur.next = cur.next
                else: self.head = cur.next
                ###########
                break
            pre_cur = cur; cur = cur.next
        if target_bt:
            for child in target_bt.get_children():
                self.push(child)
        #find new min
        self._update()
        return res

    def pop(self):
        cur = self.head
        if not cur: raise ValueError("No!")
        self.head = cur.next; cur.next = None;
        self._update()
        return cur

    def show_roots(self):
        res1 = []; res2 = []
        cur = self.head
        while cur: res1.append(cur.peak()); res2.append(len(cur)); cur = cur.next
        print("Roots' values: ", *res1)
        print("Roots' sizes", *res2)
        return

    def peek(self):
        if self.peak: return self.peak
        else: raise ValueError("No Elements")

def merge(bh_1, bh_2):
    bh_1.meld(bh_2)
    bh_2 = None
    return bh_1
