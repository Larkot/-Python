def my_func(first_mum,second_num,third_num):
    if first_mum >=second_num and second_num <= third_num:
        result  = first_mum + third_num
        return result
    elif first_mum >= third_num and second_num >=third_num:
        result = first_mum + second_num
        return result
    else:
        result = second_num + third_num
        return  result

print(my_func(5,5,4))