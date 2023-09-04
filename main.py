def name(name):
     print(f"my name is {name}")
 myname = input("enter your name")
name(myname)
 def my_meal(food,drink):
     print(f"i like to eat {food} while drinking {drink}")
 food = input("enter your favorite food")
 drink = input("enter your favorite drink")




 my_meal(food,drink)
def cube(number):
    return print(number **3)
def by_three(number1):
    if number1 % 3 == 0:
        cube(number1)
    else:
        print("false")

by_three(2)