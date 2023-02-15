def set_reducer(inp):

#input = list
#output = taking the list and reducing the number of occurences and repeating the process 
#create a new list to append
#loop through the numbers 
#count variable
#compare adjacent numbers(using indices)
#check the length of the new list
#if length > 1, repeat.
#if length - 1, return the number

    l = []

    i = 0

    while i <len(inp):
        count = 1
        while i + 1 < len(inp) and inp[i] == inp[i+1]:
            count += 1
            i += 1
        l.append(count)
        i += 1
    if len(l) == 1:
        return l[0]
    else:
        return set_reducer(l)

# set_reducer([0, 4, 6, 8, 8, 8, 5, 5, 7])