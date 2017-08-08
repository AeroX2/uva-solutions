#!/bin/env python

from math import sqrt

class Tree:

    def __init__(self, unique_id):
        self.unique_id = unique_id
        self.branches = [] 

    def add_branch(self, branch):
        self.branches.append(branch)

    def __eq__(self, other):
        return self.unique_id == other.unique_id

def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

seen = {}
def find_tree_doctor(start_tree, trees_o, doctors, min_t, min_d):
    if (len(trees_o) <= 0):
        return False

    if (start_tree.unique_id in seen):
        return False
    seen[start_tree.unique_id] = None

    #print(trees[0])
    trees = trees_o[:]
    trees.remove(start_tree)

    for branch in start_tree.branches:
        for doctor in doctors:
            if (distance(doctor, branch) <= min_d):
                return True

        for tree in trees:
            for other_branch in tree.branches:
                if (distance(branch, other_branch) <= min_t):
                    output = find_tree_doctor(tree, trees, doctors, min_t, min_d)
                    if (output):
                        return output
    return False


def main():
    for _ in range(int(input())):
        n,m,k,d = map(int, input().split())
        #print(n,m,k,d)

        doctors = []
        for _ in range(m):
            x,y = map(int,input().split())
            doctors.append((x,y))

        trees = []
        for i in range(n):
            tree = Tree(i)
            #Branches
            for _ in range(int(input())):
                x,y = map(int, input().split())
                tree.add_branch((x,y))
            trees.append(tree)
        
        #for tree in trees:
        #    print(tree.unique_id)

        global seen
        seen = {}
        if (find_tree_doctor(trees[0], trees, doctors, k, d)):
            print('Tree can be saved :)')
        else:
            print('Tree can\'t be saved :(')
main()
