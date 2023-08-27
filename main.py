my_name = input("what is your name")
my_age =("what is your age")
print(f"My name is {my_name} and I am {my_age} years old") 
first_number = int (input ("enter the first number"))
second_number = int(input ("enter the second_number"))
operation = input("enter your operation")
if operation == "+":
    print("first_number+second_nuumber")
elif operation == "-":
    print(first_number - second_number)
elif operation == "/":
    print("first_number / second_number")
elif operation == "*":
    print("first_number * second_number")
bus_capacity = 30
peopleinbus = int (input("emter the amount of passengers insid the bus :"))
peoplewantbus = int (input("enter the amount of people that want to enter yhe bus :"))
empty_seats = bus_capacity - peopleinbus
if empty_seats > peoplewantbus:
    print(f"ther are {empty_seats} empty seats")
else:
    print("the bus is full")