#Q1:

# groceries = { 
# "Baby Spinach": 2.78, 
# "Hot Chocolate": 3.70, 
# "Crackers": 2.10, 
# "Bacon": 9.00, 
# "Carrots": 0.56, 
# "Oranges": 3.08 
# } 


# aux = len(groceries)
# counter2 = 0
# quantities = []
# amount = 0

# for x in groceries:
#     qty = input("How many units did you buy?: ")
#     qty = int(qty)
#     groceries[x] = groceries[x] * qty
#     amount = amount + groceries[x]

# print("\n")
# print("\n")    
# print("====Izzy's Food Emporium==== ")

# for item, price in groceries.items(): #.items is a specific function in dictionaries
#     print(f"{item:<20} ${price:.2f}")

# print ("============================ ")
# print (f"                     ${amount:.2f}")

#Q2

# cohort = {}

# names = [ 
# "Maddy", "Bel", "Elnaz", "Gia", "Izzy", 
# "Joy", "Katie", "Maddie", "Tash", "Nic", 
# "Rachael", "Bec", "Bec", "Tabitha", "Teagen", 
# "Viv", "Anna", "Catherine", "Catherine", "Debby", 
# "Gab", "Megan", "Michelle", "Nic", "Roxy", 
# "Samara", "Sasha", "Sophie", "Teagen", "Viv" 
# ] 

# for x in names:
#     if x in cohort:
#         cohort[x] = cohort[x] + 1
#     else:
#         cohort[x] = 1

# for name, qty in cohort.items():
#     print(name, qty)


#Q3
import csv

def read_csv_file(filepath): 
    coloursX = []
    
    with open(filepath) as csv_file:
        reader = csv.reader(csv_file)
        
        for line in reader:
            coloursX.append(line)
   
    return coloursX

colour = {}
l1 = []
l2 = []
counter = 0
c2 = 0
c3 = 0


l1 = read_csv_file("colours_20.csv")



for item in l1: #l1 is a list of lists, where each list is a line from the csv
    if c3 == 0: # the first line defines the dict keys 
        while counter < 9: 
            a = item[counter]
            colour[a] = 0   # init the dictionary keys, all with values = 0
            counter = counter + 1
    
    else: # the other lines define the dict values 
        while c2 < 9: # the number 9 here comes from the fact that there are 9 elements on each line
            for x in colour:
                colour[x] = item[c2] # override the original value of zero with a value from the line
                c2 = c2 + 1 
    
    l2.append(colour) # this appends each dict to a list, in order to create a list of dict
    print("\n")
    print(colour)
    c3 = c3 + 1
    c2 = 0

# print (l2)











