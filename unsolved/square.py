import copy

def create_sides(numbers,group,current_group,side_length):
    #print(current_group)
    #print(numbers)
    #print(group)

    global memorization
    group_sum = sum(group)
    if (group_sum == side_length):

        for i,num in enumerate(group):
            memorization[num] = group[:i]+group[i+1:]

        #print(group)
        group = []
        group_sum = 0
        current_group += 1

    if (current_group >= 4):
        return True

    if (len(numbers) <= 0):
        return False

    for i,number in enumerate(numbers):
        if (group_sum+number > side_length):
            continue

        if (len(group) > 0 and 
                group[0] in memorization and
                number in memorization[group[0]]):
            continue

        if (create_sides(numbers[:i]+numbers[i+1:],group+[number],current_group,side_length)):
            return True
    return False

global memorization
memorization = {}

for _ in range(int(input())):
    numbers = list(map(int,input().split()))[1:]

    #print("Start",numbers)

    div,rem = divmod(sum(numbers),4)
    if (rem % 4 == 0):
        if (create_sides(numbers,[],0,div)):
            print('yes')
        else:
            print('no')
    else:
        print('no')
