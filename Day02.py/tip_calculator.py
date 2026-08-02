print("Welcome to the tip calculator!")
bill = float(input("What was the total bill $"))
tip = int(input("How much tip would you give? 10, 12 , or 15?: "))
split =int(input("How many people to split the bill?"))
n= (bill+tip)/split
print("Each person should pay: $",n)