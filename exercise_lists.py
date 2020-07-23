# Q1

foods = [ 
"orange", 
"apple", 
"banana", 
"strawberry", 
"grape", 
"blueberry", 
["carrot", "cauliflower", "pumpkin"], 
"passionfruit", 
"mango", 
"kiwifruit" 
] 

print(foods[0]) #Q1/1first item on the list
print(foods[2]) #Q1/2 third item on the list
print(foods[-1]) #Q1/3 last item on the list
print(foods[0:3]) #Q1/4prints first 3 items on the list - prints from item 0 to item 2 (3-1)
print(foods[7:10]) #Q1/5 prints from item item 7 to item 9 (10-1) 
print(foods[6][2])#Q1/6 last item in the sublist - this is because the sublist is in position [6] 


#Q2:

mailing_list = [ 

    ["Roary", "roary@moth.catchers"], 
    ["Remus", "remus@kapers.dog"], 
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"], 
    ["Biscuit", "biscuit@whippies.park"], 
    ["Rory", "rory@whippies.park"]
]

print(f"{mailing_list[0][0]}: {mailing_list[0][1]}")
print(f"{mailing_list[1][0]}: {mailing_list[1][1]}")
print(f"{mailing_list[2][0]}: {mailing_list[2][1]}")
print(f"{mailing_list[3][0]}: {mailing_list[3][1]}")


#Q3

names = []
name1 = input("What is your name? ")
name2 = input("What is the name of one of your friends? ")
name3 = input("What is the name of another friend? ")

names.append(name1)
names.append(name2)
names.append(name3)

print(names) 

#Q4
st1 = input("Please enter a string of text: ")
st2 = st1.split() #splits string by white spaces

print(f"{len(st2)} {st2}")

st3 = list(st1) #when applying list to a string, every character will be an item in the list
print(f"{len(st3)} {st3}")
