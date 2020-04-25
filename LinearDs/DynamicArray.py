import os
import sys

class DynamicArray:

    # initialize #
    def __init__(self, num):
        self.array = [None]*num
        self.size = 0
        self.capacity = num

    # magic #
    def __str__(self):
        return " ".join(map(str, self[:self.size]))

    def __iter__(self):
        i = 0
        while i < len(self):
            yield self.array[i]
            i += 1

    def __contain__(self, v):
        for elem in self:
            if elem == v: return True
        return False

    def __len__(self):
        return self.size

    # indexing #
    def __getitem__(self, given): # implement slice, tuple, list and int #
        if isinstance(given, tuple):
            res = []
            for elem in given:
                res.append(self.__getitem__(elem))
            return tuple(res)

        elif isinstance(given, slice):
            res = []
            step = given.step if given.step else 1
            if step == 0: print("STEP CANNOT BE 0"); return
            elif step > 0:
                start = given.start if given.start else 0
                end = given.stop if given.stop else self.size
                i = max(0, start); end = min(len(self), end)
                while i < end:
                    res.append(self.array[i]); i += step
            else: # step < 0
                start = given.start if given.start else self.size
                end = given.stop if given.stop else 0
                i = min(len(self), start); end = max(0, end)
                while i > end:
                    res.append(self.array[i]); i += step
            return res

        elif isinstance(given, list):
            res = []
            for elem in given:
                res.append(self.__getitem__(self, elem))
            return res

        elif isinstance(given, int):
            if given < 0: given += len(self)
            if given >= self.size or given < 0: print("IT IS OUT OF BOUND"); return
            return self.array[given]

        else: raise ValueError("THIS INDEXING IS INAPPROPRIATE")

    def __setitem__(self, given, given_v):

        if isinstance(given, tuple):
            for g, g_v in zip(given, given_v): self.__setitem__(g, g_v)

        elif isinstance(given, slice):
            if isinstance(given_v, int):
                step = given.step if given.step else 1
                if step == 0: print("STEP CANNOT BE 0"); return
                elif step > 0:
                    start = given.start if given.start else 0
                    end = given.stop if given.stop else self.size
                    i = max(0, start); end = min(len(self), end)
                    while i < end:
                        self.array[i] = given_v; i += step
                else: # step < 0
                    start = given.start if given.start else self.size
                    end = given.stop if given.stop else 0
                    i = min(len(self), start); end = max(0, end)
                    while i > end:
                        self.array[i] = given_v; i += step
            else: print("IT IS NOT POSSIBLE")

        elif isinstance(given, list):
            if len(given) != len(given_v): print("IT IS IMPOSSIBLE"); return
            for g, g_v in zip(given, given_v):
                if g < 0: g += len(self)
                if g < 0 or g >= len(self): continue
                self.array[g] = g_v
        elif isinstance(given , int):
            if given >= self.size: print("IT IS OUT OF BOUND"); return
            self.array[given] = given_v

        else: raise ValueError("THIS SETTING IS INAPPROPRIATE")

    def _move_array(self):
        new_array = [None]*self.capacity
        for i in range(0, len(self)): new_array[i] = self.array[i]
        self.array = new_array

    def append(self, v):
        if self.size >= self.capacity:
            self.capacity *= 2; self._move_array()
        self.array[self.size] = v
        self.size += 1

    def pop(self, index = None):
        if self.size <= 0: print("IT IS EMPTY"); return
        if index is None or index == -1: # pop last element
            self.size -= 1; expel = self.array[self.size]; self.array[self.size] = None
        else:
            if index < 0: index = len(self) - abs(index)
            if index < 0 or index >= self.size: print("IT IS OUT OF BOUND"); return
            new_array = [None]*self.capacity; j = 0
            for i in range(len(self)):
                if i == index: expel = self.array[i]; continue
                new_array[j] = self.array[i]; j += 1
            self.size -= 1; self.array = new_array

        if self.size < self.capacity//4:
            self.capacity //= 2; self._move_array()

        return expel

    def count(self, value):
        res = 0
        for elem in self:
            if elem == value: res += 1
        return res

    def extend(self, other_darr, move = False): # in-place
        if len(self) + len(other_darr) < self.capacity:
            if move: self._move_array()
            for elem in other_darr: self.append(elem)
            return
        else:
            self.capacity *= 2
            return self.extend(other_darr, True)
