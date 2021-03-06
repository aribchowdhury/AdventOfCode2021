import numpy as np #np arrays are just nice in general
import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
import collections #defaultdicts, maybe counters
import functools #use @functools.lru_cache(None) above a function to keep track of all inputs and speed it up
import string #ascii_uppercase, ascii_lowercase, etc..
import itertools #itertools.product(range(a),range(b),[1,2,3]) allows for nested for loops in one line essentially
from copy import deepcopy #deepcopy() let's use copy a list without reference areas
#Sets are POG {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))

def run(filename):
    print("Running",filename+"...")

    lines = open(filename).read().splitlines()
    depth = 0
    hor = 0
    for line in lines:
        dir,num = line.split()
        num = int(num)
        if dir == "forward": hor += num
        elif dir == "down": depth += num
        else: depth -= num
    print(depth*hor)

    p2_depth = 0
    p2_hor = 0
    p2_aim = 0
    for line in lines:
        dir,num = line.split()
        num = int(num)
        if dir == "forward":
            p2_hor += num
            p2_depth += p2_aim * num
        elif dir == "down": p2_aim += num
        else: p2_aim -= num
    print(p2_hor*p2_depth)

run("example.txt")
print()
run("day2.txt")