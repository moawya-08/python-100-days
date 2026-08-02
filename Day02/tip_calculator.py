print("Welcome to the tip calculator!")
bill = float(input("What was the total bill $"))
tip = int(input("How much percent tip would you give? 10, 12 , or 15?: "))
split =int(input("How many people to split the bill?"))
tip_percentage =tip/100
total_tip_pecentage = tip_percentage*bill
total_bill = bill + total_tip_pecentage
person =total_bill/split
final_amount = round(person,3)
print(f"Each person should pay: ${final_amount}")
