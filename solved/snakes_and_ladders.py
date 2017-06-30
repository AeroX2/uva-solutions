

for _ in range(int(input())):
    snakes_ladders = {}
    numbers = list(map(int, input().split()))

    #print(numbers)
    for _ in range(numbers[1]):
        a,b = map(int, input().split())
        snakes_ladders[a] = b

    curr_player = 0
    players = [1] * numbers[0]

    for i in range(numbers[2]):
        n = int(input())
        if (len(players) <= 0):
            continue
        
        players[curr_player] += n
        player = players[curr_player]
        
        if (player in snakes_ladders):
            players[curr_player] = snakes_ladders[player]
            player = players[curr_player]
        if (player >= 100):
            #Read extra stuff
            for _ in range(numbers[2]-i-1):
                input()
            players[curr_player] = 100
            break
        curr_player = (curr_player +1) % len(players)

    for i,player in enumerate(players):
        print("Position of player %d is %d." % (i+1, player))
