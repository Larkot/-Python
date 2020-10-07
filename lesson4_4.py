number_list = [1,1,3,5,67,2,3,7,3,1,6,5]
new_number_list = [element for element in number_list if number_list.count(element)<2]
print(new_number_list)