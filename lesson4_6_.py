from itertools import count

for element in count(int(input('Enter first number '))):
    print(element)

from itertools import cycle

valuse_list = [457, 'Mikle', 6, True]
for element in cycle(valuse_list):
    print(element)