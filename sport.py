start = int(input("please enter start point: "))
end = int(input("Please enter end point"))
day_count = 1
while start<end:
    print(f"{day_count}: {start:.2f}")
    start = start*1.1
    day_count+=1
print(f"On {day_count} sportsmen will be win")