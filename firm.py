proceeds = int(input("Please enter profit: "))
expenses  = int(input("Please  enter lose: "))
if proceeds>expenses:
    print("You are greate!")
    profit = proceeds-expenses
    profitability = profit/proceeds*100
    persons = int(input("Please enter count of employyes: "))
    profit_by_person = profit/persons
else:
    print("You are loser")
print(f"{profitability}%")
print(profit_by_person)