"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales * 0.1
    print(bonus)
elif sales >= 1000:
    bonus = sales * 0.15
    print(bonus)

#over complicated the program, ie dont need two print(bonus), if the sales aren't less than 1000 then they will be more
# so can lose the elif statement to steamline it.