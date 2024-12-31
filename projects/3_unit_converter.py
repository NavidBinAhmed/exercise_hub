def unit_con(given_m, given_cm):

    converted_cm = given_m * 100
    converted_m = given_cm / 100
    return converted_m, converted_cm 

given_m = int(input("Enter the lenght in meter: "))
given_cm = int(input("Enter the lenght in centimeter: "))
converted_m, converted_cm = unit_con(given_m, given_cm)
print(f"The converted lenght for {given_m} meter is {converted_cm} cm and {given_cm} cm is {converted_m} meter.")