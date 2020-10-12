a = 1234
m = a%10
print(m)
a = a//10
print(a)
while a > 0:
    if a%10 > m:
        m = a%10
        print(m)
    a = a//10
    print(a)
print(m)



