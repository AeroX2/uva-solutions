
def max_destinations(list1, list2, switch):
    print()

    common_element = None
    for e in list1:
        if e in list2:
            common_element = e
            break

    if (common_element is None):
        return 0
    
    p1 = list1.index(common_element)
    p2 = list2.index(common_element)

    print(common_element)

    cities = 0
    #switch = True
    while (p1 < len(list1) and p2 < len(list2)):

        if (switch):
            if (list1[p1] == list2[p2]):
                print("Switch",p1,p2,switch)
                cities += 1
                switch = not switch
            p1 += 1
        else:
            if (list1[p1] == list2[p2]):
                print("Switch",p1,p2,switch)
                cities += 1
                switch = not switch
            p2 += 1
            
    return cities

case = 0
mom = input()
while (mom != '#'):
    dad = input()

    cities1 = max_destinations(mom, dad, False)
    cities2 = max_destinations(mom, dad, True)
    cities3 = max_destinations(dad, mom, False)
    cities4 = max_destinations(dad, mom, True)
    
    print("Case #%d: you can visit at most %d cities" % (case+1,max(cities1,cities2,cities3,cities4)))

    case+=1
    mom = input()
