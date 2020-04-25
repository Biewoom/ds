import sys
import os

class DisjointSet:

    class Node:

        # magic methods #
        def __init__(self, id):
            self.id = id
            self.parent = None
            self.blocks = set() # id set
            self.children = set() # node set
            # only for root #
            self.members = set([id]) #id set

        def __str__(self):
            return 'Node id: %d, size: %d'%(self.id, len(self.members))

        def __hash__(self):
            return hash(self.id)

        def __len__(self):
            return len(self.members)

        # compare methods #
        def __eq__(self, other_node):
            return self.id == other_node.id
        def __gt__(self, other_node):
            return self.id > other_node.id
        def __ge__(self, other_node):
            return self.id >= other_node.id

        # private methods #
        def _find_parent(self):
            if self.parent is None: return self
            else: return self.parent._find_parent()

        def _adopt(self, child):
            child.parent = self
            self.children.add(child)
            if len(child.members): self.members = self.members.union(child.members); child.members = set()
            return

        def _block(self, other):
            if self == other: return
            self.blocks.add(other.id)

        def _deletememberid(self, id):
            self.members.discard(id)

        def _delete(self):
            if self.parent is None: #it is root # pick new root randomly
                self._deletememberid(self.id)
                new_node = self.children.pop(); new_node.parent = None
                new_node.members = new_node.members.union(self.members)
                while self.children: new_node._adopt(self.children.pop())
                return new_node
            else:
                p = self._find_parent()
                p._deletememberid(self.id)
                while self.children: p._adopt( self.children.pop() )
                self.parent.children.discard(self)
                return None

        # showing methods #
        def _showmembers(self):
            if self.parent is None: return self.members.copy()
            else: return self.parent._showmembers()

        def _showblock(self):
            return self.blocks.copy()

        # boolean #
        def _isitroot(self):
            if self.parent is None: return True
            else: return False
        def _isitleaf(self):
            if len(self.children) <= 0: return True
            else: return False

    # magic #
    def __init__(self):
        self.rootSet = set() # Node set
        self.memberDict = dict() # Node set

    def __len__(self): # the number of groups
        return len(self.rootSet)

    def __str__(self):
        return 'there are %d groups and %d members: '%(len(self.rootSet), len(self.memberDict))
    # helper methods #
    def _invalid(self, v):
        if v not in self.memberDict: print("The User <%d> does not exist"%(v)); return True
        else: return False

    def _union(self, p1, p2) -> Node: # Union by size, smaller rank -> taller rank
        if p1.parent is not None: raise ValueError("It is not root!")
        if p2.parent is not None: raise ValueError("It is not root!")

        if len(p1) <= len(p2):
            p2._adopt(p1)
            return p1
        else:
            p1._adopt(p2)
            return p2

    # update #
    def make_connection(self, connection):
        v1, v2 = connection
        if v1 == v2: print("we cannot make connection myself"); return
        # if it is already existed
        Node1 = None; Node2 = None;
        if v1 not in self.memberDict: self.memberDict[v1] = self.Node(v1); self.rootSet.add(self.memberDict[v1])
        Node1 = self.memberDict[v1]
        if v2 not in self.memberDict: self.memberDict[v2] = self.Node(v2); self.rootSet.add(self.memberDict[v2])
        Node2 = self.memberDict[v2]

        x = Node1._find_parent()
        y = Node2._find_parent()

        if x != y: # if there are disconnected
            _smaller = self._union(x, y)
            self.rootSet.discard(_smaller)

    def block(self, connection):
        v1, v2 = connection
        if v1 == v2: print("We cannot blocks myself"); return
        if self._invalid(v1): return
        if self._invalid(v2): return
        self.memberDict[v1]._block(self.memberDict[v2])
        return "The User <%d> block other User <%d>"%(v1, v2)

    def delete(self, v):
        if self._invalid(v): return
        node = self.memberDict[v]
        #coner-case It is root and leaf
        if node._isitleaf() and node._isitroot():
            del self.memberDict[v]
            self.rootSet.discard(node)
            return
        else:
            del self.memberDict[v]
            new_node = node._delete()
            if new_node: #It is root
                self.rootSet.discard(node); self.rootSet.add(new_node)

    def liberate(self, v):
        self.delete(v)
        self.memberDict[v] = self.Node(v)
        self.rootSet.add(self.memberDict[v])



    # show function #
    def show_myfriends(self, v1):
        # go to root and show members but exclude myself, block_list
        if self._invalid(v1): return
        node = self.memberDict[v1]
        blockSet = node._showblock()
        blockSet.add(node.id)
        members = node._showmembers()
        while blockSet: members.discard(blockSet.pop())
        return " ".join(map(str, list(members)))

    def show_groupsize(self, v1):
        if self._invalid(v1): return
        Rootnode = self.memberDict[v1]._find_parent()
        return 'My group Size: %d'%len(Rootnode)

    def show_blocks(self, v1):
        if self._invalid(v1): return
        blockSet = self.memberDict[v1]._showblock()
        return " ".join(map(str, list(blockSet)))

    def showAll(self):
        roots = self.rootSet.copy(); res = 0;
        # print("Groups' size: ", len(roots))
        while roots:
            r = roots.pop()
            members = r._showmembers()
            # print("Group <%d> with %d: "%(r.id, len(members)), members)
            res += len(members)
        print("Total Member: %d, roots's Member: %d"%(len(self.memberDict), res))
