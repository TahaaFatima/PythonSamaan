this_list = ["apple", "banana","cherry","orange","kiwi","melon","mango"]
list_two = this_list.copy()
list_three = list(this_list)
# print(list_two)
this_list[1] = "strawberry"
print(list_two)
print(list_three)