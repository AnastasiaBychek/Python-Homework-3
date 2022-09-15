my_list = [2,5,3,4,6]
def poduct_item(my_list):
    reversed_list = my_list[::-1]
    new_list = []
    for i in range(len(my_list)//2):
          new_list.append(my_list[i]*reversed_list[i])
    return new_list
print(poduct_item(my_list))
