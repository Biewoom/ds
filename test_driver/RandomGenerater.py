import os
import sys
import re
import random


def make_randomlist(n, start_int, end_int):
    res = []
    for i_iter in range(n):
        res.append( random.randint(start_int, end_int) )
    return res

def make_randomString(n, String_list):
    res = []
    for i_iter in range(n):
        res.append( String_list[random.randint(0, len(String_list)-1)] )
    return res


def make_randomTuple(n, start_int, end_int):
    res = []
    for i_iter in range(n):
        res.append( ( random.randint(start_int, end_int), random.randint(start_int, end_int) ) )
    return res

def make_tuple(start_int, end_int):
    return ( random.randint(start_int, end_int), random.randint(start_int, end_int) )

def make_int(start_int, end_int):
    return random.randint(start_int, end_int)

def make_random_call(func_list, start_int, end_int):
    return random.choice(func_list)(start_int, end_int)

def make_None(start_int, end_int):
    return None

def make_slice(start_int, end_int):
    # make step
    step = random.choice([make_None, make_int])(start_int, end_int)
    start = random.choice([make_None, make_int])(start_int, end_int)
    stop = random.choice([make_None, make_int])(start_int, end_int)
    return slice(start, stop, step)
