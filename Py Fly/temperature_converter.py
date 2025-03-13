def convert_temp(temp, unit):
    '''this function converts temperature from Celcius to Farenheit'''
    if unit=='C':
        return temp* 9/5 + 32 ## C to F
    elif unit=='F':
        return (temp-32)*5/9 ## F to C
    else:
        return None
    
print(convert_temp(25, 'C'), "F")
print(convert_temp(77, 'F'), "C")

'''output:
77.0 F
25.0 C'''