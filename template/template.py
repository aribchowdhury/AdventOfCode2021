import scipy.ndimage as sp, numpy as np #np arrays are just nice in general and scipy.ndimage correlate and convolve
import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
import collections #defaultdicts, maybe counters
import functools #use @functools.lru_cache(None) above a function to keep track of all inputs and speed it up
import math, string #ascii_uppercase, ascii_lowercase, etc..
import itertools #itertools.product(range(a),range(b),[1,2,3]) allows for nested for loops in one line essentially
import networkx #Networkx for graph problems like connected components
from copy import deepcopy #deepcopy() let's use copy a list without reference areas
#Sets are POG {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))

def run(filename):
    print("Running",filename+"...")

    #lines = open(filename)
    #lines = open(filename).read().split('\n\n')
    lines = open(filename).read().splitlines()
    #lines = list(map(int,lines))

    for line in lines:
        #a,b = line.split()
        pass


run("example.txt")
print()
run("day.txt")