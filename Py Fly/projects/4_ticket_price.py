## determine the ticket price based on the age and studentship

age = int(input("Enter age: "))
is_student = input("Are you a student? (yes/no): ").lower()

if age < 5:
    ticket = "Free"
elif age <= 12:
    ticket = "10 Tk"
elif age <= 17:
    if is_student == 'yes':
        ticket = "10 Tk"
    else:
        ticket = "20 Tk"
        
elif age <= 64:
    if is_student == 'yes':
        ticket = "12 Tk"
    else:
        ticket = "22 Tk" 

else:
    ticket = "25 Tk"
    
print(f"Fare is {ticket}.")