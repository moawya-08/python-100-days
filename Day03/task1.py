height = int(input("Enter the height: "))
age = int(input("Enter age :"))

if height >= 120:
    if age<=12 :
        print("$5")
    elif age <= 18:
        print("$7")
    else:
        print("$12")
else:
    print("Sorry Grow taller kid You can't ride")
