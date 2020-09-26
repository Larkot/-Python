first_num = int(input("First number: "))
second_num = int(input("Second number: "))
def divide (first_num,second_num):
    if second_num == 0:
        print("You cant divide by zero")
    else:
        result = first_num/second_num
        return result

print(divide(first_num,second_num))