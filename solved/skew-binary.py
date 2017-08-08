
n = int(input())
while (n != 0):
    i = 0
    final = 0
    while (n > 0):
        i += 1
        n,m = divmod(n,10)
        
        final += m*(pow(2,i)-1)
    print(final)
    
    n = int(input())    
