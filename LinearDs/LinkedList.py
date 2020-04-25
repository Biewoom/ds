import os
import sys
import re
import math

class LinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __contain__(self):

    def __

    def __str__(self):
        res = []; cur = self.head;
        while cur: res.append(cur.Out()); cur = cur.next;
        returnStr = " ".join(map(str, res) )
        return return

    def push(self, data):
        cur = self.head; New_node = self.Node(data);
        if not cur: self.head = New_node; self.size += 1; return
        while cur.next: cur = cur.next
        cur.next = New_node; self.size += 1;
        return

    def pop(self, index = None):
        cur = self.head;
        if cur == None: raise ValueError("No Node")
        self.head = cur.next; self.size -= 1
        return cur.data
