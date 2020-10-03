def sum():
    sum =0;
    exit = False
    while exit == False:
        print("For exit press Q")
        number = input("Number: ").split()
        result = 0
        for elem in range(len(number)):
            if number[elem] =="q" or number[elem]=="Q":
                exit = True
                break
            else:
                result = result+ int(number[elem])
        sum = sum + result
        print(f"Now sum is {sum}")
    print(f"Total {sum}")

sum()
