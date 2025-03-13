
''' 
1. Problem Statement: Counter:
Python script to print the integers in the specified range.

Cases:   
    2) For no parameters given, it will print 1, 2, 3, 4, 5.
    3) If only one parameter is entered, it will print 1, 2, 3, ... until that parameter is included.  __PASS
    4) If there are two or more parameters entered, it will take the first parameter as the start __PASS
        and the second parameter as the end inclusively. If they are equal, one number will be printed. __ PASS
    5) The second parameter could be less than the first parameter. __PASS

Given end_case:
    Assume that there are no invalid inputs from the user, i.e., all parameters are integers.
'''

import sys

def counter(beginner=1, finisher=5):
    step = 1 if beginner <= finisher else -1

    for i in range (beginner, finisher+step, step):
        print(i)


if __name__ == "__main__":
    args = sys.argv[1:]


    if len(args) == 0:
        counter()

    elif len(args) == 1:
        counter(1, int(args[0]))

    else:
        counter(int(args[0]), int(args[1]))




