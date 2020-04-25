import os
import sys

class DoubleLinkedList:

    class Node:
        def __init__(self, v):
            self.prev = None
            self.next = None
            self.value = v

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        res = []
        for x in self: res.append(x)
        return " ".join(map(str, res))

    def __getitem__(self, index):
        if index > 0 and index >= self.size: raise ValueError("OUT OF BOUND")
        if index < 0 and abs(index) > self.size: raise ValueError('OUT OF BOUND')
        if index >= 0:
            cur = self.head; i = 0;
            while cur:
                if i == index: return cur.value
                cur = cur.next; i += 1
        else:
            cur = self.tail; i = 1;
            while cur:
                if i == abs(index): return cur.value
                cur = cur.prev; i += 1

    def __setitem__(self, index, v):
        if index > 0 and index >= self.size: raise ValueError("OUT OF BOUND")
        if index < 0 and abs(index) > self.size: raise ValueError('OUT oF BOUND')
        if index >= 0:
            cur = self.head; i = 0;
            while cur:
                if i == index: cur.value = v; return
                cur = cur.next; i += 1
        else:
            cur = self.tail; i = 1;
            while cur:
                if i == abs(index): return cur.value
                cur = cur.prev; i += 1

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def appendright(self, v):
        new_node = self.Node(v)
        if self.size:
            cur = self.tail; cur.next = new_node; new_node.prev = cur; self.tail = new_node; self.size += 1
        else:
            self.head = self.tail = new_node; self.size += 1

    def appendleft(self, v):
        new_node = self.Node(v)
        if self.size:
            cur = self.head; cur.prev = new_node; new_node.next = cur; self.head = new_node; self.size += 1
        else:
            self.head = self.tail = new_node; self.size += 1

    def popleft(self):
        if self.size:
            cur = self.head
            return_v = cur.value
            if cur.next: self.head = cur.next; self.head.prev = None;
            else: self.head = self.tail = None
            self.size -= 1
            return return_v
        else:
            raise ValueError('OUT OF BOUND')

    def popright(self):
        if self.size:
            cur = self.tail
            return_v = cur.value
            if cur.prev: self.tail = cur.prev; self.tail.next = None;
            else: self.head = self.tail = None
            self.size -= 1
            return return_v
        else:
            raise ValueError('OUT OF BOUND')
