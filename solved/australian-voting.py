#!/bin/env python

from collections import Counter,OrderedDict

def next_line():
    try:
        return input().strip()
    except:
        return None

#TODO Pretty terrible code, should have used a class
def eliminate_candidates(candidates, votes, previous_winners):
    count = Counter()
    for vote in votes:
        for preference in vote:
            if preference in candidates:
                count[preference] += 1
                break

    thing = list(map(lambda x: (previous_winners.get(x[0],0),x), count.items()))
    sorted_list = sorted(thing, key=lambda x: (x[0],x[1][1]))

    winners = []
    total_votes = len(votes)
    for max_item in reversed(sorted_list):
        if (max_item[1][1] > total_votes/2.0):
            winners.append(max_item[1][0])
        else:
            break

    eliminated = []
    min_value = sorted_list[0]
    for min_item in sorted_list:
        if (min_item[0] == min_value[0] and min_item[1][1] == min_value[1][1]):
            eliminated.append(min_item[1][0])
        else:
            break
    else:
        winners = eliminated[:]
        eliminated = []

    not_eliminated = list(filter(lambda x: not x in eliminated, count.keys()))
    for candidate in not_eliminated:
        previous_winners[candidate] += 1 

    return eliminated,winners,previous_winners


def main():
    cases = int(next_line())
    input()
    for i in range(cases):

        candidates = OrderedDict()
        for ii in range(int(next_line())):
            candidates[ii+1] = next_line()

        votes = []
        line = next_line()
        while (line != '' and line is not None):
            vote = tuple(map(int,line.split()))
            votes.append(vote) 
            line = next_line()

        winners = []
        previous_candidates = Counter()
        while len(winners) <= 0:
            eliminated,winners,previous_candidates = eliminate_candidates(candidates, votes, previous_candidates)
            if (len(eliminated) > 0):
                for candidate in eliminated:
                    del candidates[candidate]

        winners = map(lambda x: candidates[x], winners)
        print('\n'.join(sorted(winners, key=lambda x: list(candidates.values()).index(x))))
        if (i != cases-1):
            print()

main()


