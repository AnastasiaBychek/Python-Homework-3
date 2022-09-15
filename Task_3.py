initial_list = [1.1, 1.2, 3.1, 5, 10.01]
def difference(initial_list):
    new_list = []
    for i in range(len(initial_list)):
        new_list.append(round(initial_list[i]-int(initial_list[i]),2))
    print(new_list)
    max = new_list[0]
    min = new_list[0]
    for j in range(len(new_list)):
        if max < new_list[j] and new_list[j] !=0:
            max = new_list[j]
        if min > new_list[j] and new_list[j] !=0:
            min = new_list[j]
    diff = max - min
    print(max)
    print(min)
    return diff     
print(difference(initial_list))