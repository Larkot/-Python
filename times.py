seconds = int(input("Seconds: "))
hours = seconds//3600
minutes = (seconds-hours*3600) //60
second = seconds %60
print(f"{hours}:{minutes}:{second}")