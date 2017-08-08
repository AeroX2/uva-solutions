#!/bin/env python

import sys
from collections import defaultdict

def get_lines():
    string = sys.stdin.read().strip()
    for line in string.split('\n'):
        yield line
    yield None

lines = get_lines()
line = next(lines)
next(lines)
for _ in range(int(line)):
    fallen_trees = defaultdict(set)

    line = next(lines)
    while (line != '' and line is not None):
        person,tree = map(int, line.split())
        fallen_trees[person].add(tree)
        line = next(lines)
    print(fallen_trees)


