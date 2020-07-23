#Q1
count = 0
num1 = input ("Please enter a number: ")

while len(num1) >= 1 :
    count = int(num1) + count
    num1 = input ("Please enter a number: ")

print(count)


#Q2
mailing_list = [ 

    ["Roary", "roary@moth.catchers"], 
    ["Remus", "remus@kapers.dog"], 
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"], 
    ["Biscuit", "biscuit@whippies.park"], 
    ["Rory", "rory@whippies.park"]
]

for item in mailing_list:
    print(f"{item[0]}: {item[1]}")


#Q3
names = []
counter = 0


while counter < 3:
    name1 = input ("Please enter a name: ")
    names.append(name1)
    counter = counter + 1

for name in names:
    print(name)


#Q4
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
    groceries[counter2][1] = groceries[counter2][1] * qty
    amount = amount + groceries[counter2][1]
    counter2 = counter2 + 1

print("\n")
print("\n")    
print("====Izzy's Food Emporium==== ")

for item in groceries:
    print(f"{item[0]:<20} ${item[1]:.2f}")


print ("============================ ")
print (f"                     ${amount:.2f}")