# EXERCISE 1: Variables and user inputs
# Q1

print("EXERCISE 1: Variables and user inputs")
print("Q1 Part 1")
num1 = input("Please enter one number: ")
num2 = input("Please enter a second number: ")
addme = int(num1) + int(num2)
print(f"those two numbers added result in {addme}")

print("Q1 Part 2")
num3 = input("Please enter one number: ")
num4 = input("Please enter a second number: ")
addme2 = int(num3) + int(num4)
print(f"those two numbers added result in {addme2}")

print("Q1 Part 3")
num5 = input("Please enter one number: ")
num6 = input("Please enter a second number: ")
addme3 = float(num5) + float(num6)
print(f"those two numbers added result in {addme3}")

# Q2
print("Q2 Part 1")
num7 = input("Please enter one number: ")
num8 = input("Please enter a second number: ")
mult1 = int(num7) * int(num8)
print(f"{num7} * {num8} = {mult1}")

print("Q2 Part 2")
num9 = input("Please enter one number: ")
num10 = input("Please enter a second number: ")
mult2 = int(num9) * int(num10)
print(f"{num9} * {num10} = {mult2}")

print("Q2 Part 3")
num11 = input("Please enter one number: ")
num12 = input("Please enter a second number: ")
mult3 = float(num11) * int(num12)
print(f"{num11} * {num12} = {mult3}")

# Q3
print("Q3 Part 1")
d1 = input("Please enter distance1 in km: ")
metres = 1000 * int(d1)
cmetres = 100 * metres
print(f"{d1}km = {metres}m")
print(f"{d1}km = {cmetres}cm")

print("Q3 Part 2")
d2 = input("Please enter distance2 in km: ")
metres2 = int(1000 * float(d2))
cmetres2 = int(100 * metres2)
print(f"{d2}km = {metres2}m")
print(f"{d2}km = {cmetres2}cm")

# Q4
print("Q4 Part 1")
name1 = input("Please enter your name: ")
h1 = input("Please enter your height in cm: ")
print(f"{name1} is {h1}cms tall")

print("Q4 Part 2")
name2 = input("Please enter your name: ")
h2 = input("Please enter your height in cm: ")
print(f"{name2} is {h2}cms tall")

##################################################
# EXERCISE 2: Booleans and if statements
# Q1

print("EXERCISE 2: Booleans and if statements")
print("Q1")

moths_in_house = False

if moths_in_house:
    print("Get the moths!")
else:
    print("No threats detected. ")

# Q2

print("Q2")
moths_in_house = False
mitch_is_home = True

if moths_in_house & mitch_is_home:
    print("Hooman! Help me get the moths")

if (not moths_in_house) & (not mitch_is_home):
    print("No threats detected. ")

if moths_in_house & (not mitch_is_home):
    print("Meoooooow! Hisssss!")

if (not moths_in_house) & mitch_is_home:
    print("Climb on Mitch")


# Q3
print("Q3")

light_colour = "Green"
car_detected = False

if light_colour == "Red":
    if not (car_detected):
        print("Do nothing.")

    if car_detected:
        print("Flash!")

if light_colour == "Green" or light_colour == "Amber":
    print("Do nothing.")


# Q4
print("Q4")
h3 = input("Please enter your height in cm: ")
h3 = int(h3)

if h3 >= 120:
    print("Hop on!")

else:
    print("Sorry, not today :(")

















