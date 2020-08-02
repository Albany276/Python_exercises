#Q1
# def tempF2C (temp_F):
#     temp_C = (temp_F -32) * 5/9
#     temp_C = round(temp_C)
#     return temp_C

# aux = tempF2C(113)
# print(f"the answer is: {aux} Celsius")


#Q2

# def be_mean(sum1, num_items):
#     mean1 = sum1 / num_items
#     return mean1

# sum1 = 0
# counter = 0
# num1 = input ("Please enter a number: ")

# while len(num1) >= 1 :
#     sum1 = int(num1) + sum1
#     num1 = input ("Please enter a number: ")
#     counter = counter + 1

# aux1 = be_mean(sum1, counter)
# print(f"The mean is {aux1}")


#Q3

# import csv

# def read_csv_file(filepath): 
#     coloursX = []
    
#     with open(filepath) as csv_file:
#         reader = csv.reader(csv_file)
        
#         for line in reader:
#             coloursX.append(line)
   
#     return coloursX


# def format_colour_line(colour_data, col1, col2, col3): 

#     for item in colour_data:
#         print(f"{item[col1]:<20} {item[col2]:<20} {item[col3]:<20} ")

# l1 = []
# l1 = read_csv_file("colours_213.csv")
# format_colour_line(l1, 1, 2, 4)



#Q4

def calculate_cost(unit_price, number_purchase): 
    a = unit_price * number_purchase
    return  a

groceries = [ 
    ["Baby Spinach", 2.78], 
    ["Hot Chocolate", 3.70], 
    ["Crackers", 2.10], 
    ["Bacon", 9.00], 
    ["Carrots", 0.56], 
    ["Oranges", 3.08] 
] 

aux = len(groceries)
counter2 = 0
quantities = []
amount = 0

while counter2 < aux:
    qty = input("How many units did you buy?: ")
    qty = int(qty)
    groceries[counter2][1] = calculate_cost(groceries[counter2][1], qty)
    amount = amount + groceries[counter2][1]
    counter2 = counter2 + 1

print("\n")
print("\n")    
print("====Izzy's Food Emporium==== ")

for item in groceries:
    print(f"{item[0]:<20} ${item[1]:.2f}")


print ("============================ ")
print (f"                     ${amount:.2f}")














