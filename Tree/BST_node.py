import os
import sys
import re
import math

class BST:
    class Node:
        # attributes #
        def __init__(self, id):
            self.id = id
        # swap #
        def swap(self, other_node):
            self.id, other_node.id = other_node.id, self.id

        # compare #
        def __eq__(self, other_node):
            return self.id == other_node.id
        def __lt__(self, other_node):
            return self.id < other_node.id
        def __gt__(self, other_node):
            return self.id > other_node.id
        def __ge__(self, other_node):
            return self.id >= other_node.id
        def __le__(self, other_node):
            return self.id <= other_node.id

    # attributes #
    def __init__(self):
        self.root = None #node
        self.left_child = None #subtree
        self.right_child = None #subtree
        self.size = 0
    def __str__(self):
        return "size : %d and root's value : %d and there are four travarsals"%(len(self), self._rootID())
    def __len__(self):
        return self.size

    # state #
    def _leaf(self):
        if not self.left_child and not self.right_child: return True
        else: return False
    def _rootID(self):
        if not self.root: return 0
        return self.root.id
    def _skew(self):
        hasleft = 1 if self.left_child else 0
        hasright = 1 if self.right_child else 0
        if hasleft|hasright and hasleft^hasright:return True
        else: return False

    # utility method #
    @staticmethod
    def _len(Tree):
        if Tree: return len(Tree)
        else: return 0
    def _findMinTree(self)->Node:
        if not self.root: raise ValueError("No root")
        if not self.left_child: return self.root
        else: return self.left_child._findMinTree()
    def _isleftchild(self, child):
        if self.left_child and self.left_child.root == child.root: return True
        else: return False

    # update #
    def insort(self, id):
        # if it is empty tree #
        self.size += 1
        if not self.root: self.root = self.Node(id)
        else:
            if id < self._rootID():
                if not self.left_child: self.left_child = BST()
                self.left_child.insort(id)
            elif id > self._rootID():
                if not self.right_child: self.right_child = BST()
                self.right_child.insort(id)
            else: # it is same # skew
                if not self.left_child:
                    self.left_child = BST(); self.left_child.insort(id)
                else:
                    new_bt = BST(); new_bt.insort(id)
                    new_bt.left_child = self.left_child; new_bt.size += len(self.left_child)
                    self.left_child = new_bt;

    def _pop(self, parent = None):
        #empty
        if not self.root: raise ValueError('EMPTY')
        self.size -= 1; res = self._rootID(); changed_tree = None
        if self._leaf():
            if not parent: self.root = None; return res
        elif self._skew():
            if self.left_child: changed_tree = self.left_child
            else: changed_tree = self.right_child
        else:
            MinNode = self.right_child._findMinTree()
            self.root.swap(MinNode)
            self.right_child.delete(MinNode.id)
            return res

        if parent:
            if parent._isleftchild(self): parent.left_child = changed_tree
            else: parent.right_child = changed_tree
        else: self = changed_tree

        return res

    def delete(self, id, parent = None):
        if not self.root: raise ValueError('EMPTY')
        if id < self._rootID():
            if not self.left_child: return -1
            res = self.left_child.delete(id, self)
            self.size -= 1 if res > 0 else 0
            return res
        elif id > self._rootID():
            if not self.right_child: return -1
            res = self.right_child.delete(id, self)
            self.size -= 1 if res > 0 else 0
            return res
        else:
            if self.left_child and id == self.left_child._rootID():
                self.size -= 1; return self.left_child.delete(id, self)
            else: self._pop(parent); return 1

    def update(self, id1, id2):
        if self.delete(id1) < 0: return 'No id1: %d'%id1
        self.insort(id2)
        return 'Update Success'
    # lookup #
    def bisect_left(self, id): #find and return index
        if id < self._rootID():
            if not self.left_child: return self._len(self.left_child)
            return self.left_child.bisect_left(id)
        elif id > self._rootID():
            if not self.right_child: return self._len(self.left_child) + 1
            return self._len(self.left_child) + 1 + self.right_child.bisect_left(id)
        else: #if id == self._rootID()
            if self.left_child and id == self.left_child._rootID(): return self.left_child.bisect_left(id)
            else:
                return self._len(self.left_child)

    def bisect_right(self, id): #find and return index
        if id < self._rootID():
            if not self.left_child: return self._len(self.left_child)
            return self.left_child.bisect_right(id)
        elif id > self._rootID():
            if not self.right_child: return self._len(self.left_child) + 1
            return self._len(self.left_child) + 1 + self.right_child.bisect_right(id)
        else: # if id == self._rootID()
            return self._len(self.left_child) + 1

    # utility #
    def inorder_trav(self):
        if not self.root: return ""
        res = str(self._rootID())
        if self.left_child: res = self.left_child.inorder_trav() + " " + res
        if self.right_child: res = res + " " + self.right_child.inorder_trav()
        return res
    def reverse_trave(self):
        if not self.root: return ""
        res = str(self._rootID())
        if self.right_child: res = self.right_child.reverse_trave() + " " + res
        if self.left_child: res = res + " " + self.left_child.reverse_trave()
        return res

    def preorder_trav(self):
        if not self.root: return ""
        res = str(self._rootID())
        if self.left_child: res = res + " " + self.left_child.preorder_trav()
        if self.right_child: res = res + " " + self.right_child.preorder_trav()
        return res

    def postorder_trav(self):
        if not self.root: return ""
        res = ""
        if self.left_child: res = self.left_child.postorder_trav() + " " + res
        if self.right_child: res = self.right_child.postorder_trav() + " " + res
        res = res + str(self._rootID())
        return res

    def bfs_trav(self):
        if not self.root: return ""
        res = ""; Q = []; Q.append(self)
        while Q:
            cur = Q.pop(0); res = res + str(cur._rootID()) + " ";
            if cur.left_child: Q.append(cur.left_child)
            if cur.right_child: Q.append(cur.right_child)
        return res
