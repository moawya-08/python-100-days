# def format_name(f_name, l_name):
#     formatted_f_name =f_name.title()
#     formatted_l_name= l_name.title()
#     return formatted_f_name , formatted_l_name

# print(format_name("moaWYa", "Shariff"))

def is_leap_year(year):
    # Write your code here. 
    leap = ""
    if year % 4 == 1:
        leap = False
    elif year % 4 == 0:
        if year % 100 == 1:
            leap = True
        elif year % 100 == 0:
            if year % 400 == 1:
                leap = False
            elif year % 400 == 0:
                leap = True
    return leap
is_leap_year(2026)