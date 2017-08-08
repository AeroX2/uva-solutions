#!/bin/env python

def distance(clip, movie, i, clip_len):
    movie >>= i
    mask = (1 << clip_len)-1
    movie &= mask

    haming_distance = movie ^ clip

    haming_distance = bin(haming_distance).count('1')
    return haming_distance

def main():
    m,q = map(int, input().split())

    movies = [input().strip() for _ in range(m)]
    clips = [input().strip() for _ in range(q)]

    for clip in clips:
        min_haming = None
        min_index = None

        clip_len = len(clip)
        clip = int(clip,2)

        for i,movie in enumerate(movies):
            movie_len = len(movie)
            movie = int(movie,2)

            for ii in range(movie_len-clip_len+1):
                haming_distance = distance(clip, movie, ii, clip_len)
                if (min_haming is None or haming_distance < min_haming):
                    min_haming = haming_distance
                    min_index = i+1

        print(min_index)

main()
