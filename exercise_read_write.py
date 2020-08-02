#Q1

names = []
counter = 0
with open("names.txt") as txt_file: #the open command seems to load the file line by line - by default it opens the file in reading mode
    # print(txt_file)
    for line in txt_file:
        line = line.strip() #removes the new line (\n) character
        names.append(line)

for name in names:
    counter = counter + 1
    print(f"{counter}. {name}")

#Q2
import csv
colours20 = []
colours213 = []

with open("colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours20.append(line)

for item in colours20:
    print(f"{item[1]:<20} {item[2]:<20} {item[4]:<20} ")

with open("colours_213.csv") as csv_file2:
    reader = csv.reader(csv_file2)
    for line in reader:
        colours213.append(line)

print("\n")
for item in colours213:
    print(f"{item[1]:<20} {item[2]:<20} {item[4]:<20} ")

#Q3

# The find() method returns an integer value:
# If the substring exists inside the string, it returns the index of the first occurence of the substring.
# If substring doesn't exist inside the string, it returns -1.

red_counter = 0
green_counter = 0
blue_counter = 0

for item in colours20:
    if item[4].find("red") > 0:
        red_counter = red_counter + 1

    if item[4].find("green") > 0:
        green_counter = green_counter + 1

    if item[4].find("blue") > 0:
        blue_counter = blue_counter + 1

print("\n Colours_20 Results")
print(f"Red: {red_counter}")
print(f"Green: {green_counter}")
print(f"Blue: {blue_counter}")


red_counter2 = 0
green_counter2 = 0
blue_counter2 = 0

for item in colours213:
    # print(item[4])

    if item[4].find("red") > 0:
        red_counter2 = red_counter2 + 1


    if item[4].find("green") > 0:
        green_counter2 = green_counter2 + 1

    if item[4].find("blue") > 0:
        blue_counter2 = blue_counter2 + 1

print("\nColours_213 Results")
print(f"Red: {red_counter2}")
print(f"Green: {green_counter2}")
print(f"Blue: {blue_counter2}")

