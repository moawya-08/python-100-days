bill=1
print("Welcome to the python pizza deliveries")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperonie in your pizza? Typpe Y for yes and N for no : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")
if size == "S":
    bill+= 15

elif size == "M":
    bill+= 20

elif size == "L":
    bill+=25

if pepperoni == "Y":
    if size == "S":
         bill+=2
    else:
        bill+=3

if extra_cheese == "Y":
    bill+=1

print(f"Your total bill is ${bill}")
