my_list = [2,4,5,6,7,3,6]
def sum_item(my_list):
    sum = 0
    for i in range(len(my_list)):
        if i%2 != 0:
            sum = sum + my_list[i]
    return sum
print(sum_item(my_list))