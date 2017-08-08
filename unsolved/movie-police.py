#!/bin/env python

def main():
    m,q = map(int, input().split())

    movies = [int(input(),2) for _ in range(m)]
    clips = [int(input(),2) for _ in range(q)]

    for clip in clips:

        min_haming = None
        min_index = None

        print("Clip", bin(clip))
        for i,movie in enumerate(movies):

            for ii in range(movie.bit_length()-clip.bit_length()+1):
                haming_distance = (clip << ii) ^ movie
                haming_distance &= ~((1 << i) - 1)
                haming_distance = bin(haming_distance).count('1')

                if (min_haming is None or haming_distance < min_haming):
                    min_haming = haming_distance
                    min_index = i+1
        print(min_index)

main()
