list_numbers = [13,4,8,7,11,6,5]
new_list_number = [el for num,el in enumerate(list_numbers) if list_numbers[num-1]<list_numbers[num]]
print(f"{list_numbers}")
print(f"{new_list_number}")