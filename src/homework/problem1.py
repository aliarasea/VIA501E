# A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99 items, the
# cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a program that takes
# how many items are bought as an input and prints the total cost.



def price(itemCount):
    if itemCount < 10:
        return 12
    elif itemCount >= 10 and itemCount < 100:
        return 10
    else:
        return 7


def problem1():
    itemCount = int(input("Enter the number of items bought: "))
    totalCost = itemCount * price(itemCount)
    print(f"The total cost is: ${totalCost}")


while (exit := input("Do you want to calculate the total cost? (y/n): ")) == 'y':
    problem1()