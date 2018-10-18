import copy

def recursion(letters, contraints, final):

    for contraint in reversed(contraints):
        try:
            a = final.index(contraint[0])
            b = final.index(contraint[2])
            if (a > b):
                return None
        except:
            pass
    
    if (len(letters) <= 0):
        return [final]

    output = []
    for i,letter in enumerate(letters):
        result = recursion(letters[:i]+letters[i+1:], contraints, final+[letters[i]])
        if (result):
            output.extend(result)

    return output

n = int(input())
for i in range(n):
    input()
    letters = input().split()
    contraints = input().split()

    result = recursion(sorted(letters), contraints, [])
    if (len(result) > 0):
        for line in result:
            print(' '.join(line))
    else:
        print('NO')

    if (i != n-1):
        print()
