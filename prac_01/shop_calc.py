#number_of_items = int(input('Enter number of items:  '))
#price_of_item_a = float(input('enter price: '))
#price_of_item_b = float(input('enter price: '))
#price_of_item_c = float(input('enter price: '))

#total_price_for_items = price_of_item_a + price_of_item_b + price_of_item_c
#if number_of_items >= 0:
#    print("number of items:{}".format(number_of_items))
#    print("price of item:${}".format (price_of_item_a))
#    print("price of item:${}".format (price_of_item_b))
#    print("price of item:${}".format (price_of_item_c))
#    print("total price for {} items:${}" .format(number_of_items, total_price_for_items))
#should have been a for i in range progarm



"""CP1404/CP5632 - Practical - Suggested Solution
Shop calculator program to determine total (discounted) price
"""

total = 0
number = int(input("Number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for i in range(number):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9  # apply 10% discount

print("Total price for ", number, " items is $", total, sep='')

# with string formatting for currency output
print("Total price for {} items is ${:.2f}".format(number, total))total += price