#!/bin/env python

from collections import Counter

def next_line():
    try:
        return input().strip()
    except:
        return None

def eliminate_candidates(candidates, votes):
    count = Counter()
    for vote in votes:
        for preference in vote:
            if preference in candidates:
                count[preference] += 1
                break

    #print(votes)
    print("Count", count)

    print(candidates)

    total_votes = len(votes)
    sorted_list = sorted(count.items(), key=lambda x: x[1])

    print(sorted_list)

    min_value = sorted_list[0][1]

    eliminated = []
    for min_item in sorted_list:
        if (min_item[1] == min_value):
            eliminated.append(min_item[0])
        else:
            break

    winners = []
    for max_item in reversed(sorted_list):
        if (max_item[1] > total_votes/2.0):
            winners.append(max_item[0])
        else:
            break

    if (len(eliminated) == total_votes):
        winners = eliminated[:]
        eliminated = []

    print(eliminated, winners)

    return eliminated,winners


def main():
    for z in range(int(next_line())):
        if z == 0:
            input()

        candidates = {}
        for i in range(int(next_line())):
            candidates[i+1] = next_line()
        #print(candidates)

        votes = []
        line = next_line()
        while (line != '' and line is not None):
            vote = tuple(map(int,line.split()))
            votes.append(vote) 
            line = next_line()

        while True:
            eliminated,winners = eliminate_candidates(candidates, votes)
            if (len(winners) > 0):
                #print("Winners", winners)
                #print("Cand", candidates)
                blub = []
                for x in winners:
                    blub.append(candidates[x])
                print('\n'.join(sorted(blub)))
                print()
                break
            else:
                for x in eliminated:
                    del candidates[x]

main()


