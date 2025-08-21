import random

try:
    ch = "y"
    while ch == "y":
        num_rolls = int(input("How many times you want to roll Dice:"))
        for i in range(num_rolls):
            dice_num = random.randint(1, 6)
            print(f"Roll {1} : You Got ->{dice_num}")
        ch = input("Do You want To Continue [Y/n]:").casefold()
    print("Thank You!See You next Time")
except Exception as e:
    print("You Did something SUS :( i.e --> ", e)
