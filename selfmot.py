# here we practice some coding exercise: DSA, Leetcode, etc besides dev

'''def nav(list_user):
    summation = 0

    for elements in list_user:
        summation += elements

    return summation

check = nav([12,3,4,5,2])
print(check)'''

'''write a function that

1. prints the sum of numbers
2. prints the max value
3. prints the min value
4. prints the second largest number
5. prints the reversed number''' 

'''def sum_num(list):

    summation = 0

    for elements in list:
        summation += elements

    return summation

list = [1,2,3]
print(sum_num(list))'''

'''def max_value(list):

    maximum = 0

    for elements in list:
        if elements >= maximum:
            maximum = elements
    
    return maximum

list = [1,2,3,6,4,7]
print(max_value(list))'''

'''def min_value(list):

    minimum = float('inf')

    for elements in list:
        if elements <= minimum:
            minimum = elements

    return minimum

list = [7,2,3,4]
print(min_value(list))'''


'''def second_largest(list_input):


    first, second = float('-inf'), float('-inf')

#[1,2,3]--for 1 in list: if 1 > -inf, 
    for elements in list_input:
        if elements > first:
            second = first
            first = elements

#[1,2,4,3]--- 4 > 3 > new sec
        elif first > elements > second:
            second = elements

    return second

print(second_largest(list_input=[1,2,3,4,5,6,7,8]))'''


'''def reversed_number(list_input):

    reversed_list = []

    for elements in list_input[::-1]:
        reversed_list.append(elements)

    return reversed_list

given_list = [1,2,43,21,4,2]
print(reversed_number(given_list)) '''

#sum
'''def summation(input_list):
    sum_input = 0

    for elements in input_list:
        sum_input += elements
    return sum_input

given_list = [1,2,3,4,5] 
print(summation(given_list))'''

#leetcode palindrome problem
'''class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 :
            return False
        
        number = x
        reverse = 0

        while number:
            reverse = reverse * 10 + number % 10
            number //= 10

        return x == reverse
    
check = Solution()
print(check.isPalindrome(-121))
    
#leetcode fibonacci
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return fib.self[n-2] + fib.self[n-1]

print(Solution.fib(2,3))
'''


#python tutorial.py
#https://www.youtube.com/watch?v=rfscVS0vtbw
#4:15- inheritance
'''
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)
'''

'''
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
result = num1 + num2
print(result)
'''
'''
#madlibs game
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
'''
'''
#lists
friends = ["Kevin", "Karen", "Jim", 2, True]
print(friends)
print(friends[4])

relatives = ["Kevi", "Kare", "Ji", 4, False]

full= friends + relatives
print(full[1:3])

full[0]= "Navid"
print(full)
'''

'''#list function
lucky_numbers = [4, 5, 2, 6, 1]
lucky_numbers.reverse()
print(lucky_numbers)

friends = ["Kevin", "Karen", "Jim", "Jim"]
friends.sort()
friends.reverse()
f2 = friends.copy()
print(f2)

friends = ["Kevin", "Karen", "Jim", "Jim"]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.pop()  #removes the last value
'''

'''
#tuple: immutable (it is as it is)
coordinates = (4, 5)
print(coordinates)
index = coordinates[1]
print(index)
coordinates[1] = 10
'''

#function
'''def sayhi():
    print("Hi")
sayhi()
'''

#parameterize
'''def say_hi(name, age):
    print("hello user, " + name + ". You are " + str(age)+ ".")

say_hi("Mike", 24)
say_hi("Navid", 34)'''

#returning value: alternative of a calculation or print statement inside function
'''def cube(num):
    return num*num*num
    #a = num*num*num
    #print(a)
print(cube(4))
#cube(3)'''

'''#if-else
a ='im hungry'
if a =="im hungry" :
    print("I eat breakfast")
else:
    print("none")


is_male = False

if is_male:
    print("You are a male")
else:
    print("None")'''


'''def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(354,400,25))'''

#better calculator 1
'''def calculator(num1: int, num2: int, num3: int):
    sum = num1 + num2 + num3
    diff = num2 - num1
    div = num3/num1
    mul = num1*2
    #return sum, diff, div, mul

    print("the results are: " + str(sum) + "," + str(diff) + "," + str(div) + "," + str(mul))

calculator(12,36,48)'''

#better calculator 2
'''num1 = int(input("Enter first number: "))
op = input("Enter operator: ")
num2 = int(input("Enter second number: "))

if op == '+':
    sum = num1 + num2
    print("summation is " + str(sum))

elif op == '-':
    diff = num1 - num2
    print("difference is " + str(diff))

elif op == '*':
    mul = num1 * num2
    print("product is " + str(mul))

elif op == '/':
    div = num1 / num2
    print("quotient is " + str(div))

else:
    print("Invalid operator")'''

#dictionaries- introduction
'''di = {'name': 'navid', 'age': '34', 'city': 'Dhaka', 'religion': 'Islam', 'marital': 'single'}

print(f"The person is {di['name']} and he is {di['marital']}.")

print(di['name'], di['age'])'''


#dictionaries- month
'''month = {1: 'January', 'feb': 'February', 'mar': 'March', 'apr': 'April', 'may': 'May', 'jun': 'June', 'jul': 'July', 'aug': 'August',
         'sep': 'September', 'oct': 'October', 'nov': 'November', 'dec': 'December'}

print(month['mar'])
print(month.get(1))
print(month.get('Luv', 'Not valid key'))
print(month.get('jan', 'the first month'))'''

#while loop:
'''i = 1

while i <= 10:
    print(i)
    i += 1

print("Done with loop")
'''

#guessing game
'''secret_word = 'dog'
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses. You lose!")
else:
    print("You win!")
'''

'''secret_word = "cat"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, You lose.")
else:
    print("You win!")'''


'''secret_word = "cat"
guess = ""

while guess != secret_word:
    guess = input("Enter guess: ")

print("You win!")'''


#for loop
'''list = ['apple', 'orange', 'mango', 'guava']
len(list)
for fruits in range(len(list)):
    print(list[fruits])
'''
'''for letter in "Navid Bin Ahmed":
    print(letter)
'''

#looping using index
'''list = ['apple', 'orange', 'mango', 'guava']
len(list)
for fruits in range(len(list)):
    print(list[fruits])'''


#exponent - function
'''num = (2, 4, 5, 6, 3)

def raise_power():
    for nums in num:
        print(nums**3)

raise_power()
'''
#exponent - function - base power
'''def raise_power(base, power):
    #print(base**power)
    #return
    return print(base**power)
raise_power(2,5)
'''
#exponent - function - base power
'''def raise_power(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result

print(raise_power(3,4))'''

#exponent - function - base power
'''def raise_to_power(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result
print(raise_to_power(2,3))'''

#exponent - for loop
'''num = [3,5,6,7]

for nums in num:
    print(nums**3)'''


#2D array list
'''number_grid = [
    [1,2,4],
    [2,4,5],
    [4,2,4],
    [0,3]
]
print(number_grid[0][0])
print(number_grid[1][1])
print(number_grid[3][0])
'''

#nested for loop- loop inside loop
'''number_grid = [
    [1,2,4],
    [2,4,5],
    [4,2,4],
    [0,3]
]

for row in number_grid:    #shows full matrix, output = as it is 2D array
    #print(row)
    for col in row:        #shows each element in specific row, output = individual all elements
        print(col)'''

#2D array and nested loop
'''number_grid = [
    [1,3,4],
    [4,5,2],
    [2,4,5]
]

for row in number_grid:
    print(row)
    for col in row:
        print(col)'''

#translator 2:57

'''def translate(phrase):
    translation = " "
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter

    return translation

print(translate(input("Enter a phrase: ")))'''

'''def translate(phrase):
    tranlation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            tranlation = tranlation + "k"
        else:
            tranlation = tranlation + letter
    return tranlation
print(translate(input("Enter a phrase: ")))'''


#a basic translator
'''def translator(phrase):
    translation = ""

    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "k"
        else:
            translation = translation + letter
    return translation

print(translator(input("Enter a phrase: "))) 
'''

'''def translator(phrase):
    translation = ""

    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translator(input("Enter a phrase: ")))''' 

#try except
# dealing with error, value error for example
'''try:
    value = 10/0 #divisionbyzero error
    number = int(input("enter a number: "))
    print(number)

except ZeroDivisionError as err:
    print("Division by zero error")  #for 10/0 problem

except ValueError:
    print("Invalid input")
'''

#reading, writing, creating, appending files
'''file = open("text.txt", "a")
file.write("\n<p> This is a paragraph.</p>")

file.close()'''

#modules and pip - importing functions from external file: usteful_tool
#modules- file
#package - multiple modules/files
'''file = open("usteful_tool.py", "w")
file.close()'''

'''import usteful_tool
a = usteful_tool.roll_dice(10)
print(a)
b = usteful_tool.get_file_ext("sanik.txt")
print(b)'''

'''import operator
x = int(input("enter x: "))
y = int(input("enter y: "))
a = operator.add(x,y)
print("Addition is :", a)'''


#classes and objects
#creating a student file as class
'''file = open("student.py", "w")
file.close()
'''
#importing and creating object for the student class
'''from student import Student

student1 = Student("Navid", 2.5, "Science", True)
print(student1.name)
print(student1.gpa)
print(student1.on_probabtion)
print(student1.subject)'''


#create a class and object for person: name and age
#creating class file
'''file = open("person.py", "w")
file.close()'''

#by importing and creating object
'''from person import Person

attendee_1 = Person("John", 27, "Boston", "Single", "Married")
print("Relationship status of the person is: ", attendee_1.relationship)
print("Name and age of the attendee: ", attendee_1.name, attendee_1.age)
'''

#by directly writing class and object
'''class Person:

    def __init__(self, name, age, location, relationship, education):
        self.name = name
        self.age = age
        self.location = location
        self.relationship = relationship 
        self.education = education 

attendee_1 = Person("John", 27, "Boston", "Single", "Married")
print("Relationship status of the person is: ", attendee_1.relationship)
print("Name and age of the attendee: ", attendee_1.name, attendee_1.age)
'''


#mcq quiz
'''questions = [
    "What color are skies?\n (a)Red\n (b)Blue\n (c)Green\n\n",
    "What color is the blood?\n (a)Green\n (b)Red\n (c)Blue\n\n",
    "What color is the grass?\n (a)Red\n (b)Greed\n (c)Blue\n\n"
]

from question import Question

ques = [
   Question(questions[0], "b"),
   Question(questions[1], "b"),
   Question(questions[2], "b") 
]

def run_quiz(ques):
    score = 0
    for questions in ques:
        answer = input(questions.prompt)
        if answer == questions.answer:
            score += 1
    print("You got: " + str(score) + "/" + str(len(ques)) + " correct")
run_quiz(ques)'''

#quiz
'''questions = [
    "What color are apples?\n (a)Red/Green\n (b)Purple\n (c)Orange\n\n",
    "What color are bananas?\n (a)Teal\n (b)Magenta\n (c)Yellow\n\n",
    "What color are strawberries?\n (a)Yellow\n (b)Red\n (c)Blue\n\n"  
]

from question import Question

questions = [
    Question(questions[0], "a"),
    Question(questions[1], "c"),
    Question(questions[2], "b")
]

def run_test(questions):
    score = 0

    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got: " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
'''

#class method object
'''class Car:
    # Define attributes
    color = "red"
    brand = "Toyota"

    # Define a method
    def start_engine(selfabc):
        print("Engine started!")

# Create an object of the Car class
my_car = Car()

# Accessing attributes
print(my_car.color)  # Output: red

# Calling methods
my_car.start_engine()  # Output: Engine started!
'''

#check wheather the student is in honor roll
'''from student import Student

student1 = Student("Oscar", 3.10, "Accounting",  False)
student2 = Student("Phyllis", 3.80, "Business", True)

print(student2.on_honor_roll())'''

#class, object and inheritance
'''class Car:
    def __init__(self, window, door, engine):
        self.window = window
        self.door = door
        self.engine = engine

    
    def driving(self):
        print("Let's drive the car")'''

#audi is inherited from the parent Car class, with additional parameter 'horsepower'
'''class Audi(Car):
    def __init__(self, window, door, engine, horsepower):
        super().__init__(window, door, engine)
        self.horsepower = horsepower
    

    def selfdriving(self):
        print("It is a self driving car.")

audiq7 = Audi(4, 5, "Diesel", 200)

print(audiq7.horsepower)
print(audiq7.window)
print(audiq7.driving())
print(audiq7.selfdriving())

car1 = Car(4,5,"Diesel")
print(car1)
print(audiq7)

print(dir(audiq7))'''

#inheritance
'''from chef import Chef

myChef = Chef()
myChef.make_chicken()
myChef.make_pasta()

#we can print this way too
Chef().make_chicken()
Chef().make_pasta()
'''

#create a car class and inherid audi from it
'''class Car:
    def __init__(self, window, door, engine):
        self.window = window
        self.door = door
        self.engine = engine

    def drive(self):
        print("Let's drive the car.")

class Audi(Car):
    def __init__(self, window, door, engine, speed):
        super().__init__(window, door, engine)
        self.speed = speed

    def selfdrive(self):
        print("Audi is self driving car.")

audi7 = Audi(4, 5, "Diesel", 6)

print(audi7.door)
print(audi7.window)
print(audi7.engine)
'''
#create BMW class inherited from Car class 
'''class BMW(Car):
    def __init__(self, window, door, engine):
        super().__init__(window, door, engine)

bmw = BMW(3, 4, "Electric")
print(bmw.window)
print(bmw.door)
print(bmw.engine)
'''

#create class and call object from it
'''class Car:
    def __init__(self, window, door):
        self.window = window
        self.door = door

    #method
    def runfast(self):
        print("The car runs fast.")

audi = Car(4, 5)
#print(audi.window)
#my_car = Car(4, 6)
audi.runfast()'''

#Most asked interview ques from medium - link later: class object
# Ex- 1 Original code and the mistake in it: Attribute error
'''class MyClass:
    def __init__(self):
        self.__variable = 42

obj = MyClass()
print(obj.__variable)
'''
#as the name mangling changes the attribute as _MyClass__variable
#so the following should work
'''class MyClass:
    def __init__(self):
        self.__variable = 42
obj = MyClass()
print(obj._MyClass__variable)'''

#alternatively, another corrected form                 
'''class MyClass:
    def __init__(self):
        self.__variable = 42

    def get_variable(self):
        return self.__variable

obj = MyClass()
print(obj.get_variable())

#Output 42'''

#exercise 2
'''class A:
    def __init__(self):
        self.__variable = 42
    

    def display(self):
        print(self.__variable)   #name mingling problem unless we return it
        #return self.__variable  #not working

class B(A):                     #B is inherited by A
    def __init__(self):
        super().__init__()
        self.__variable = 99


obj = A()
obj.display()

obj2 = B()
obj.display()

#prints 42 not 99. Because A calls display method first even it has name mingling.
'''

#will it work removing super init? yes
'''class A:
    def __init__(self):
        self.__variable = 42
    

    def display(self):
        print(self.__variable)   #name mingling problem unless we return it
        #return self.__variable  #not working

class B(A):                     #B is inherited by A
    def __init__(self):
        #super().__init__()
        self.__variable = 99


obj = A()
obj.display()

obj2 = B()
obj.display()
'''
#@classmethod is python decorator telling interpreter to treat it like a class method
'''class A:
    count = 0

    def __init__(self):
        A.count += 3

    @classmethod
    def get_count(cls):
        return cls.count
    
obj_one = A()
obj_two = A()

print(obj_one.get_count())
print(obj_two.get_count())

#output 6'''

'''class A:
    count = 0
    
    def __init__(self):
        self.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count
    
obj_one = A()
obj_two = A()
print(obj_one.get_count())
print(obj_two.get_count())'''


#write an example of Student class and create object for 3 students, with a method
#Show example for inheritance
'''class Student:
    def __init__(self, name, subject, marks):
        self.name = name
        self.subject = subject
        self.marks = marks
    
    @classmethod
    def honor(self):
        print("Top students in the class!")

class HighGPA(Student):
    def __init__(self, name, subject, marks, grade):
        super().__init__(name, subject, marks)
        self.grade = grade 

    @classmethod
    def honor(self):
        print("He is the topper!")

first = HighGPA("Akib", "Math", 99, "A+")
second = HighGPA("Tamim", "English", 91, "A+")
third = HighGPA("Labib", "Bangla", 92, "A+")

print(second.name)
print(third.grade)
print(first.name)
HighGPA("Akib", "Math", 99, "A+").honor()
'''
#write an example of Student class and create object for 3 students, with a method
#Show example for inheritance
#class attributes
'''class Person:
    name = "Navid"
    occupation = "Scientist"
    networth = 100

a = Person()
print(a.name, a.occupation)

a.name = "Sakin"
a.occupation = "Accountant"
print(a.name, a.occupation)
'''

#instance attributes
'''class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

first = Person("Navid", "Scientist")
second = Person("Sakin", "Developer")
print(first.name, first.occupation)
print(second.name, second.occupation)
'''

#this should work as well when instance attributes can be customized by passing 
#arguments to the constructor (__init__) when creating instances of the class
'''class Person:
    def __init__(self, name = "Navid", occupation = "Scientist"):
        self.name = name
        self.occupation = occupation

#first = Person("Navid", "Scientist")
#second = Person("Sakin", "Developer")
first =  Person()
print(first.name, first.occupation)
#print(second.name, second.occupation)'''

#create class with method, and create its instance/object with inheritance
'''class Restaurant:
    def __init__(self, pizza, tea, beaf, juice):
        self.pizza = pizza
        self.tea = tea
        self.beaf = beaf
        self.juice = juice
    
    @classmethod
    def order(self):
        print("Order is placed.")

#creating object
Royal_Cafe = Restaurant("Pizza", "Malai Tea", "Pasta", "Malta")
print(Royal_Cafe.pizza)
print(Royal_Cafe.beaf)
print(Royal_Cafe.juice)
Restaurant("Pizza", "Malai Tea", "Pasta", "Malta").order()
'''

#creating a class for reataurant and inherit it for two restaurance in Gazipur subclass 
'''class Restaurant:
    def __init__(self, pizza, tea, beaf, juice):
        self.pizza = pizza
        self.tea = tea
        self.beaf = beaf
        self.juice = juice
    
    @classmethod
    def order(self):
        print("Order is placed.")

class Gazipur(Restaurant):
    def __init__(self, pizza, tea, beaf, juice, fuska):
        super().__init__(pizza, tea, beaf, juice)
        self.fuska = fuska

Royal = Gazipur("Pizza", "Malai Tea", "Pasta", "Malta", "Doi-Fuska")
print(Royal.fuska)
print(Royal.juice)

Handi = Gazipur("Pizza", "Malai Tea", "Pasta", "Malta", "Doi-Fuska")
print(Handi.pizza)

#creating object
Royal_Cafe = Restaurant("Pizza", "Malai Tea", "Pasta", "Malta")
print(Royal_Cafe.pizza)
print(Royal_Cafe.beaf)
print(Royal_Cafe.juice)
Restaurant("Pizza", "Malai Tea", "Pasta", "Malta").order()
'''

#inheritance, object, class exercises
#https://medium.com/@zilayhuda/most-asked-python-interview-questions-part-1-classes-a27816b04bbe
#upto ex 3
'''class A:
    count = 0
    def __init__(self):
        A.count += 1
    @classmethod
    def get_count(cls):
        return cls.count
class B(A):
    pass
    def __init__(self):
        B.count += 1
a = A()
b = B()
print(a.get_count())
print(b.get_count())
'''


#write a class for mobile and add instance for 3 phones
#also inherit this to create deshi phones

'''class Mobile:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price
    
    @classmethod
    def availabilit(self):
        print("Available globally")'''

#creating instances from class

'''Samsung = Mobile("Samsung", "S7", "26,500 Tk")
iPhone = Mobile("iPhone", "15 Pro Max", "155,000 Tk")
Oppo = Mobile("Oppo", "M2", "32,500 Tk")

print(Samsung.name, Samsung.model, Samsung.price)
print(iPhone.name, iPhone.model, iPhone.price)
print(Oppo.name, Oppo.model, Oppo.price)'''

# now inherit a class named deshiphone and use the attributes with new ones

'''class Deshi(Mobile):
    def __init__(self, name, model, price, company):
        super().__init__(name, model, price)
        self.comppany = company

    def location(self):
        print("These are made in bangladesh phones.")

Walton = Deshi("Walton,", "A1,", "27,000 Tk,", "Walton Group.")
Sapphire = Deshi("Sapphire,", "AS,", "123,000 Tk,", "Sapphire Tech.")

print(Walton.name, Walton.model, Walton.price, Walton.comppany)
print(Sapphire.name, Sapphire.model, Sapphire.price, Sapphire.comppany)
'''
#the deshi class inherits 3 main properties with its own only property that is company
#the above code prints the below outputs
'''Walton, A1, 27,000 Tk, Walton Group.
Sapphire, AS, 123,000 Tk, Sapphire Tech.'''



#let's deep dive into a few more examples to assess the skill level
#1 take a list and reverse it (use for loop, use a function and do directly)

#direct
'''list = [2, 5, 6, 7, 3]

reversed_list = list[::-1]

print(reversed_list)'''


#using a for loop
'''list = [3, 5, 7, 2, 5, 4]

rev_list = []
for nums in list[::-1]:
    rev_list.append(nums)

print(rev_list)
'''

'''list = [2, 4, 6, 1, 7]

reversed_list = []
for elements in list[::-1]:
    reversed_list.append(elements)

print("Reversed list: ", reversed_list)
'''
#user sharing the list
'''input_list = input("Enter the list: ")
modified_list = [str(x) for x in input_list.split()]

reversed_list = []
for element in modified_list[::-1]:
    reversed_list.append(element)

print("Reversed list of the given string: ", reversed_list)'''

#a list of integers and returning the sum

'''list = [1, 4, 6, 1]

sum = 0
for elements in list:
    sum += elements

print(sum) '''


'''#given list
list = [2, 5, 2, 5, 2, 6]

#initialize summation
sum = 0

#use a loop for all the numbers in list
for numbers in list:
    sum += numbers

print(sum)'''

#code using a function for summation
'''def sumnum(numbers):

    summation = 0
    for number in numbers:
        summation += number
    return summation

print(sumnum([1,3,5]))'''

'''
def summation_of_numbers(numbers):

#initialization    
    summation = 0

#iteration of numbers
    for elements in numbers:
        summation += elements
#return function output
    return summation

print(summation_of_numbers([1, 5, 6, 7]))
'''


#write a function thake takes a list and prints the sum
'''def summation(list_numbers):

    sum_of_numbers = 0

    for elements in list_numbers:
        sum_of_numbers += elements

    return sum_of_numbers

print(summation([1,4,5,1,5,2,5,3,2,1]))'''


#the same problem using a function
'''def list_sum(numbers):
    return sum(numbers)

print(list_sum([2,5,6,7,2,4]))'''


'''def list_sum(numbers):
    return sum(numbers)

print(list_sum([2,5,3,2]))
'''

#removing duplicates from list given by the user
'''def remove_dup(list):
    unique_list = []
    for element in list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
user_input = input("Enter an array of numbers without comma: ")
original = [int(x) for x in user_input.split()]
new_list = remove_dup(original)
print("Original list: ", original)
print("Unique list: ", new_list)'''

#again
'''def duplicate(list):
    
    unique_list = []

    for elements in list:
        if elements not in unique_list:
            unique_list.append(elements)

    return unique_list

user_input = input("Enter a sequence of numbers: ")
original_list = [int(x) for x in user_input.split()]
new_list = duplicate(original_list)

print("Original list: ", original_list)
print("Uniqe list: ", new_list)'''

#again
'''def removeduplicates(list):
    
#initialization    
    unique_list = []

#running this loop will iterate through each values and check if the element is present
#in unique list. Otherwise it will append the unique list
    for elements in list:
        if elements not in unique_list:
            unique_list.append(elements)

    return unique_list

#given input is converted to a list, consider it an integers
user_input = input("Enter a series of number: ")
original_list = [int(x) for x in user_input.split()]

#calling function and use a variable
new_list = removeduplicates(original_list)

#printing
print("Original list is: ", original_list)
print("Unique list is: ", new_list)'''


# 2 done out of 10 practice problems shared by gpt
# https://chatgpt.com/c/74daa9d9-6334-4279-925f-ceb9c2a36b19

#list sum DSA
'''def list_sum(numbers):
    
    if not all(isinstance(number, (int, float)) for number in numbers):
        raise ValueError("Value is integer.")

    summation = 0

    for number in numbers:
        summation += number
    
    return summation

print(list_sum([1, 3, 4, 2]))'''

#remove duplicate problem
'''def remove_dup(list):

    unique_list = []

    for element in list:
        if element not in unique_list:
            unique_list.append(element)
            
    return unique_list

user_given = input("enter list: ")

original = [int(x) for x in user_given.split()]

#original = [1,3,2,4,3,4,2,3,5]

removed = remove_dup(original)

print("Original list: ", original)
print("Removed duplicates: ", removed)'''

#define a class and print the method for area
# class definition
#attributes: l, w
#method: area (beahvior of class obj)
#(object instance)
'''class Rectangle:
    def __init__(self, area, length, width):
        self.area = area
        self.length = length
        self.width = width
    
    @classmethod
    def area_rect(self, area, length, width):
        area = length*width
        print("Area is", area, "square units.")
        return area

Rectangle(12,4,7).area_rect(20, 5, 3)
'''
#define a class and print the method for perimeter
'''class perimeter:
    def __init__(self, perimeter, length, width):
        self.perimeter = perimeter
        self.length = length
        self.width = width

    @classmethod
    def perimeter_measure(self, perimeter, length, width):
        perimeter = 2*(length+width)
        print("The perimeter is", perimeter, "unit.")
        
        return perimeter

perimeter(1,2,3).perimeter_measure(23, 4, 6)
'''
#define a class for recatangualr cube and write methods for area and volume
'''class cube:
    def __init__(self, length, width, height, area, volume):
        self.length = length
        self.width = width
        self.height = height
        self.area = area
        self.volume = volume

    def measure_area(self, length, width, height, area):
        area = 2*(length*width + width*height + length*height)
        print("The surface area is", area, "square unit.")
        return area


    def measure_volume(self, lenght, width, height, volume):
        volume = lenght*width*height
        print("The volume is", volume, "cubic unit.")
        return volume
    
cube(1,2,3,4,5).measure_area(1,1,1,0)
cube(1,2,3,4,5).measure_volume(3,1,4,0)
'''

#define a class and create method to calculate area
'''class Rectangle:
    def __init__(self, length, width ):
        self.length = length
        self.width = width


    def area(self):
        return self.length * self.width

rect = Rectangle(5,4)
print(rect.area())
'''

#create student class with instance showing result status
'''class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    

    def status(self):
        if self.grade >= 80:
            print("Passed")
        else:
            print("Failed")


student1 = Student("Akib", 81).status()  #outputs Passed
student2 = Student("Noor", 76).status()  #outputs Failed
student3 = Student("Navid", 59).status() #outputs Failed''' 
#student1.status()

#Dictionary Creation: Create a dictionary from two lists, 
#one containing keys and the other containing values.

'''List1 = ["A", "B", "C", "D", "E"]
List2 = [ 3,   5,   6,   2,   5 ]

#dict (zip method is used to convert lists into dictionary)
dictionary = dict(zip(List1, List2))  
print(dictionary)'''

#again, using tuples
'''key_names = ("Aman", "Zaman", "Layden", "Alen")
value_grade = ("A+", "A", "A+", "B")

dictionary = dict(zip(key_names, value_grade))
print(dictionary)
'''

'''4. Frequency Counter: Write a function that takes a string and 
returns a dictionary with the frequency of each character.'''
'''def counter(string):
    freq = {}

    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(counter("Navid Bin Ahmed"))
'''

#Again
'''def counter(string):
    frequency = {}

    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

print(counter(" Q  "))
'''

'''def counter(string):
    freq = {}

    for char in string:
        if char in freq:
            freq [char] += 1
        else:
            freq[char] = 1

    return freq

print(counter("Navid"))'''

'''Tuples
5. Swap Tuple Elements: Write a function that takes a tuple with two elements 
and returns a new tuple with the elements swapped.
'''
'''def swap(tuple):
    return (tuple[1], tuple[0])

print(swap(('s',4)))
'''

'''def swap(tuple):
    return (tuple[1], tuple[0])

print(swap((5,7)))
'''

'''def swap(tuple):
    return (tuple[1], tuple[0])

print(swap((6,8)))
'''

'''def swap(tuple):
    return (tuple[2], tuple[1], tuple[0])

print(swap((2,5,1)))
'''

'''def swap_tuple(tuple):
    return (tuple[4], tuple[3], tuple[2], tuple[1], tuple[0])

print(swap_tuple((1,2,3,4,5)))
'''

'''list1 = ['Akib', 'Noor']
list2 = [12, 34]

dictionary = dict(zip(list1, list2))
print(dictionary)
'''

'''def counter(string):
    freq = {}

    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(counter("Navid"))
'''

#6. Tuple to String: Write a function that takes a tuple of strings and returns 
# a single string concatenated with each element.'''
'''
def tupletostring(tuple):
    return ''.join(tuple)

print(tupletostring(('h', 'e', 'l', 'l', 'o', ' ', 'r', 'u', 'm', 'a', 'n', 'a')))
'''
#manually tuple to string conversion
'''def tuple_to_string(tuple):
    result = " "

    for item in tuple:
        result += str(item)
    return result

my_tuple = ('a', 'y', ',', 'h', 'a', 'y')
result_string = tuple_to_string(my_tuple)
print(result_string)'''

# Function to convert a single element to a string manually
'''def element_to_string(element):
    if isinstance(element, int):
        # Convert integer to string manually
        result = ''
        if element == 0:
            return '0'
        if element < 0:
            result = '-'
            element = -element
        digits = []
        while element > 0:
            digits.append(chr(ord('0') + element % 10))
            element //= 10
        return result + ''.join(digits[::-1])
    
    elif isinstance(element, float):
        # Convert float to string manually
        int_part = int(element)
        frac_part = element - int_part
        int_str = element_to_string(int_part)
        frac_str = ''
        if frac_part != 0:
            frac_str = '.'
            while frac_part != 0:
                frac_part *= 10
                digit = int(frac_part)
                frac_str += chr(ord('0') + digit)
                frac_part -= digit
        return int_str + frac_str
    
    elif isinstance(element, str):
        # Strings are already strings
        return element
    
    else:
        # For unsupported types, raise an error
        raise TypeError("Unsupported element type")

# Function to convert tuple to string manually
def tuple_to_string(t):
    # Initialize an empty string to hold the result
    result = ""
    
    # Iterate through each element in the tuple
    for item in t:
        # Convert the item to a string manually and concatenate it to the result
        result += element_to_string(item)
    
    return result

# Example usage
#my_tuple = ('a', 'b', 'c', 1, 2, 3, -45, 6.78)
my_tuple = ('a', 'b', 'c')
result_string = tuple_to_string(my_tuple)
print(result_string)  # Output: 'abc123-456.78
'''

'''Sets
7. Set Intersection: Write a function that takes two sets and returns their 
intersection.'''

'''set_1 = {1, 3, 4, 5, 6, 7}
set_2 = {4, 3, 2, 6, 2, 6}

def intersection(set_1, set_2):
    return set_1 & set_2

print(intersection(set_1, set_2))
'''

'''set_1 = {1,3,4,6}
set_2 = {1,5,6,3}

def intersection(set_1, set_2):
    return set_1 & set_2

print(intersection(set_1, set_2))'''


'''8. Unique Elements: Write a function that takes a list and returns a set of 
unique elements from the list.'''

'''def unique(list):
    return set(list)

print(unique([1,2,3,4,5,6,2,4,6,3,5,2,3,5,3]))'''


'''def unique_elements(list):
    return set(list)

print(unique_elements([1,2,4,2,4,2,4,6,4,2,3,5,2,4,6]))'''


'''def unique(list):
    unique_list = []


    for items in list:
        if items not in unique_list:
            unique_list.append(items)

    return unique_list

print(unique([1,2,3,4,5,6,2,4,6,3,5,2,3,5,3]))'''


'''Classes, Methods, and Instances
9. Class Definition: Define a class Rectangle with attributes length and width. 
Include a method to calculate the area of the rectangle.
10. Class Instances: Define a class Student with attributes name and grade. 
Create instances of Student and write a method to determine if the student has 
passed based on their grade.'''

#..................................................................................
#..................................................................................
'''list = [3,5,4,6,4,7,5,7,3,5]
max_value = max(list)
print(max_value)'''


'''Create a class BankAccount with attributes account_number, account_holder, 
and balance. Add methods to deposit, withdraw, and check the balance.'''

'''class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} Tk. New balance is {self.balance} Tk.")
        else:
            print("Deposit amount must be positive.")



    def withdraw(self, amount):
        if self.balance >= amount > 0:
            self.balance -= amount       
            print(f"Withdraw {amount}. New balance is {self.balance}.")
        else:
            print("Invalid withdrawal amount.")


    def balance_check(self):
        return self.balance


account = BankAccount("12345", "Navid", 5500)
print ("Current balance is", account.balance, "Tk.")

account.deposit(1500)
account.withdraw(500)
'''

'''class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} Tk. New balance is {self.balance} Tk.")
        else:
            print("Deposited amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        print(f"Withdraw amount {amount} Tk. New balance is {self.balance} Tk.")

    def check_balance(self):
        return self.balance
    
account = BankAccount("12345", "Navid", 2000)
print("Original balance is", account.balance, "Tk.")
account.deposit(900)
account.withdraw(400)'''


'''class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} Tk. New balance is {self.balance} Tk.")
        else:
            print("Deposited amount is invalid.")


    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw amount {amount} Tk. New balance is {self.balance} Tk.")
        else:
            print("Withdraw amount is invalid.")


    def check_balance(self):
        return self.balance

account = BankAccount("Navid", "123", 2500)
print("Initial balance is", account.balance, "Tk.")
account.deposit(500)
account.withdraw(1000)'''


#finding second largest element in a list


'''def second_largest(list):
    if len(list) < 2:
        return None
    
    first, second = float('-inf'), float('-inf')
    for num in list:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second

answer = second_largest([1,4,6])
print("Second largenst element :", answer)
'''

'''def secondlargest (list):
    if len(list) < 2:
        return None 
    
    largest, second_largest = float('-inf'), float('-inf')

    for num in list:
        if num > largest:
            second_largest = largest
            largest = num

        elif largest > num > second_largest:
            second_largest = num
    return second_largest


print(secondlargest([1,2,3,4]))
print(secondlargest([1]))'''

#access tuple suing for loop
'''def access_tuple(tuple):

    last_element = None
    for element in tuple:    
        #tuple_last = tuple [-1]
        last_element = element
    return last_element

tuple = (1,2,4,5,7)
print(access_tuple(tuple))'''

#direct access to tuple
'''def access(tuple):
    return tuple[0]

tuple = (1,2,4,5)
print(access(tuple))'''


#accessing second largest number
'''def secondlargest(list):
    if len(list) < 2:
        return None
    
    largest, second_largest = float('-inf'), float('-inf')

    for number in list:
        if number > largest:
            #largest = second_largest
            second_largest = largest   # updates second largest as largest 
            largest = number           # stores current number as largest

        elif largest > number > second_largest:
            second_largest = number                   #checks if new number is larger than
    return second_largest                             # second largest
 
print(secondlargest([1,4,5,6]))
'''

#second largest from a list

'''def secondlargest(list):
    if len(list) < 2:
        return None
    
    largest, second_largest = float('-inf'), float('-inf')

    for num in list:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    return second_largest
print(secondlargest([1,3,4,5,6]))'''

'''import array
for name in array.__dict__:
    print(name)
'''


'''Write a Python function that takes two lists and returns 
True if they have at least one common member.'''


'''def have_commen_elements(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1 = [1,2,3,4]
list2 = [3,4,5,6]
list3 = [7,8,9,10]

print(have_commen_elements(list1, list2))
print(have_commen_elements(list2, list3))'''



#leetcode roman to integers

'''def roman_to_integer(roman):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    integer_value = 0
    prev_value = 0

    for symbol in reversed(roman):
        current_value = roman_values[symbol]

        if current_value >= prev_value:
            integer_value += current_value
        else:
            integer_value -= current_value

        prev_value = current_value

    return integer_value

# Test the function
print(roman_to_integer('III'))     # Output: 3
print(roman_to_integer("IV"))      # Output: 4
print(roman_to_integer("IX"))      # Output: 9
print(roman_to_integer("LVIII"))   # Output: 58
print(roman_to_integer("MCMXCIV")) # Output: 1994
'''

#leetcode, palindrome
'''def isPalindrome(x: int) -> bool:
    # Base condition
    if x < 0:
        return False
    # Store the number in a variable
    number = x
    # This will store the reverse of the number
    reverse = 0
    while number:
        reverse = reverse * 10 + number % 10
        number //= 10
    return x == reverse

print(isPalindrome(121))
'''

#leetcode palindrome problem
'''class Solution:
    def isPalindrome(self, x: int) -> bool:
#edge case
        if x < 0:
            return False
        
        number = x
        reverse = 0

        while number:
            reverse = reverse*10 + number % 10
            number //= 10

        return x == reverse
    
check = Solution()
print(check.isPalindrome(121))'''


#summation of elements in a list
'''def summation_of_list_elements(list):
    
    summation = 0
    
    for numbers in list: 
        summation += numbers

    return summation

print(summation_of_list_elements([1,2,3,4]))'''


#removing duplicates from list given by the user
'''def remove_dup(list):
    unique_list = []
    for element in list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
user_input = input("Enter an array of numbers without comma: ")
original = [int(x) for x in user_input.split()]
new_list = remove_dup(original)
print("Original list: ", original)
print("Unique list: ", new_list)'''

#leetcode 
#start from here, remove duplicates problem
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150

'''def remove_duplicates(list):
    unique_list = []

    for elements in list:
        if elements not in unique_list:
            unique_list.append(elements)
    return unique_list

list = [1,2,3,4,1,2,6]
print(remove_duplicates(list))'''


#remove duplicates
'''def remove_duplicates(list):
    
    unique_list = []

    for elements in list:
        if elements not in unique_list:
            unique_list.append(elements)

    return unique_list

print(remove_duplicates([1,2,3,4,4,4,4,1]))
'''

'''step 1- taking a list ok
step 2- run a Loop ok
step 3- build logic (initialization) ok
step 4- return
step 5- print
step 6- edge cases
step 7- test: DONE and works fine''' 

'''def remove_duplicates(inputlist):    
    

    if not all(isinstance (inputlist, (int, int)) for inputlist in inputlist):
        raise ValueError("Invalid input, put integers only.")
    
#    initialization of output
    removed_duplicates_list = []

    for elements in inputlist:
        if elements not in removed_duplicates_list:
            removed_duplicates_list.append(elements)
        
    return removed_duplicates_list

#test example
list = [1,2,3,4,5,4]
print(remove_duplicates(list))


list_2 = []
print(remove_duplicates(list_2))
 '''
 	
'''def sumnum(numbers):
    # Check for invalid inputs (optional, depends on interview requirements)
    if not all(isinstance(number, (int, float)) for number in numbers):
        raise ValueError("All elements must be integers or floats")

    # Initialize summation
    summation = 0
    # Iterate through the list and accumulate the sum
    for number in numbers:
        summation += number
    
    return summation

# Example usage (discuss verbally or write briefly if time permits)
print(sumnum([1, 2, 3]))  # Output: 6 '''



# find max value in a list
'''def maxval(input_list):
    max_value = 0

    for elements in input_list:
        if elements >= max_value:
            max_value = elements
    return max_value

print(maxval([1,2,3,4,5,6,7,8,9,10,11,12]))
'''

'''There are a few mistakes in your code:
#Initialization of max_value: It should be initialized to a very small number, 
not as an empty list.
#Comparison Logic: The comparison and assignment in the loop are incorrect. 
You should compare each element with max_value and update max_value accordingly.
#Return Value: The code should return a single value, not a list.'''

#find min value in a list
'''
def minvaliue(input_list):

# initialization to a very large positive number

    min_value = float('inf')

    for elements in input_list:
        if elements <= min_value:
            min_value = elements

    return min_value

print(minvaliue([3,4,5,6]))'''

#again
'''def minvalue(inputlist):

    min_value = float('inf')

    for elements in inputlist:
        if elements <= min_value:
            min_value = elements

    return min_value

print(minvalue([-4,2,3,4,5]))
'''

#again with unit test
'''import unittest
def min_value(input_list):
    
    minvalue = float('inf')

    for elements in input_list:
        if elements <= minvalue:
            minvalue = elements

    return minvalue

print(min_value([-2,3,4,5,6]))

class TestFucntion_sum(unittest.TestCase):

   def test_min_value(self):                                    #classmethod
        self.assertEqual(min_value([2,3,4]), 2)                 #assertion

# def test_float_value(self):     #without method for each time, assertion works fine
        self.assertEqual(min_value([1.4, 2.6, 3.0]), 1.4)

#    def test_neg_mixed(self):
        self.assertEqual(min_value([-2, -5, 3, 5, 20]), -5)

#    def test_empty_list(self):
        self.assertEqual(min_value([]), float('inf'))

#    def test_large_numbers(self):
        self.assertEqual(min_value([1e10, 2e10]), 1e10)

#    def test_sinlge_numbers(self):
        self.assertEqual(min_value([100]), 100)


if __name__ == '__main__':
    unittest.main()
'''


#finding minimum value in a list
'''1. take a list as input
2. declare min value to the most limit
3. run a loop and use condition/ logic
4. return
5. print result
6. handle edge cases'''

'''def minval(list):

    min_value = float('inf')

    for elements in list:
        if elements <= min_value:
            min_value = elements
    return min_value

print(minval([2,3,4]))
'''

#find the max value the same way
'''def maxval(list):
    max_value = 0

    for elements in list:
        #checks every iteration, if that is grreater than current max value
        if elements >= max_value:
        #the latest value from elements is stored if that is max (satisfies condition) 
            max_value = elements

    return max_value

print(maxval([1,2,3,4,8]))'''


#finding average of n numbers
'''def average(list):

    ''''''
    docstings:
    calculate the average of numbers.

    Args:
    list, a number of integers to calculate average.

    Returns:
    float, the average of numbers.

    ''''''

    summation = 0
    avg_number = 0
    n = len(list)
    
    #edge case, if no numbers are shared
    if n == 0:
        return "Nothing typed"

# running iteration
    for elements in list:
        summation += elements
#average is calculted outside for loop
    avg_number = summation / n

    return float(avg_number)

numbers = input("Give some input integers: ")
list_user = [int(x) for x in numbers.split(',')]             
result = average(list_user)
print("The average of numbers: ", result)'''

#quiz Youtube
#https://www.youtube.com/watch?v=Oo72LgwD2II&list=PLH1n1sJO7tbxmE36txTPhgidmW5Z9Bn7m&index=2


'''def remove_duplicates(list):
    unique_list = []

    for elements in list:
        if elements not in unique_list:
            unique_list.append(elements)

    return unique_list

print(remove_duplicates([1,2,3,4,4,5,4,6,6]))
'''

'''def max_value(list):

    max_element = 0

    for elements in list:
        if elements >= max_element:
            max_element = elements     

    return max_element

list_element = [2,4,28,1,9,11,1,24,7,5,2]

check = max_value(list_element)
print("The maximum value in the list: ", check)
'''

'''def min_value(list):

    min_element = float('inf')

    for elements in list:
        if elements <= min_element:
            min_element = elements     

    return min_element

list_element = [2,4,28,9,11,24,7,5,2]

check = min_value(list_element)
print("The minimum value in the list: ", check)'''


#finding second largest element in a list
'''def second_largest(list):
    if len(list) < 2:
        return None
    
    first, second = float('-inf'), float('-inf')
    for num in list:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second

answer = second_largest([1,4,6])
print("Second largenst element :", answer)
'''
 #again
'''def second_largest(list):

    if len(list) < 2:
        return None
    
    largest_number, second_largest_number = float('-inf'), float('-inf')
    for elements in list:
        if elements > largest_number:  #checks if a number is greater than largest
            second_largest_number = largest_number  #update second_largest with largest
            largest_number = elements  #update largest with elements

        elif largest_number > elements > second_largest_number:
            second_largest_number = elements    #update second largest

    return second_largest_number

check = second_largest([1,2,3,4,5, 1273638,2746823,6,3,5,3,5,6,7])
print("Second largest in list: ", check)'''

'''def second_largest(list):
    if len(list) < 2:
        return None
    
    largest, second = float('-inf'), float('-inf')

# [2,3,4,5,7] if 5 > 4, sec = 4, lar = 5
    for elements in list:
        if elements > largest:
            second = largest
            largest = elements
# -inf > 3 > 2             
        elif largest > elements > second:
            second = elements

    return second

print(second_largest([1,2,3,14,4]))
'''

'''def rev(list):
    
    reversed_list = []

    for elements in list[::-1]: #loop to iterate through the elements from end to start
        reversed_list.append(elements)  #append these in reversed list

    return reversed_list

list = [2, 4, 6, 1, 7]
check = rev(list)
print("Reversed list: ", check)
'''
'''def rev(list):
    
    reversed_list = []

    for elements in range(len(list)-1, -1, -1): #loop to iterate through the elements from end to start
        reversed_list.append(list[elements])  #append these in reversed list

    return reversed_list

list = [2, 3, 6, 1, 7, 8]
check = rev(list)
print("Reversed list: ", check)'''

#second largest
'''def second_largest(list):

    first, second = float('-inf'), float('-inf')
# [2,3,4] ----for 3 in list: 3 > 2; 
    for elements in list:
        if elements > first:
            second = first
            first = elements

        elif first > elements > second:
            second = elements

    return second

print(second_largest([1,2,7,4]))'''


#again
'''def second_largest(list):

    first, second = float('-inf'), float('-inf')


#[1,2,3,4]...for 2 in list: 2 > -inf, first = 2, 
    for elements in list:
        if elements > first:
            second = first
            first = elements
#[1,2,3,14,5] ---for 5 in list: 14>5>3
        elif first > elements > second:
            second = elements

    return second

print(second_largest([1,2,3,4,15,6]))
'''

'''def second_largest(list):
    
    ''''''
    Args: list, with a number of integers
    Return: integer, the second largest element from the input list
    ''''''

    first, second = float('-inf'), float('-inf')

    for elements in list:
        if elements > first:
            second = first
            first = elements
        
        elif first > elements > second:
            second = elements

    return second

print(second_largest([1,2,13,4]))'''


#leetcode palindrome problem
'''class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 :
            return False
        
        number = x
        reverse = 0

        while number:
            reverse = reverse * 10 + number % 10
            number //= 10

        return x == reverse
    
check = Solution()
print(check.isPalindrome(-121))'''    


#leetcode fibonacci
'''class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return fib.self[n-2] + fib.self[n-1]

print(Solution.fib(2,3))
'''

'''class Solution:
    def fibcheck(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        return self.fibcheck(x-2) + self.fibcheck(x-1)
    
print(Solution.fibcheck(4,5))
    
'''

'''class Solution:
    def __init__(self):
        self.memo = {}

    def fib(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]

print(Solution.fib(4,5))'''

'''from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        number = None
        balance = 0

        for element in nums:
            if balance == 0:
                number = element
            balance += 1 if number == element else -1
        
        return number

# Example usage:
solution = Solution()
print(solution.majorityElement([3, 2, 3]))  # Output: 3
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
'''




'''def summation(given_list):
    sum_list = 0

    for elements in given_list:
        sum_list += elements 

    return sum_list

print(summation([1,2,7,4,5]))

'''
#remove duplicate problem
'''def remove_dup(list):

    unique_list = []

    for element in list:
        if element not in unique_list:
            unique_list.append(element)
            
    return unique_list

user_given = input("enter list: ")

original = [int(x) for x in user_given.split()]

#original = [1,3,2,4,3,4,2,3,5]

removed = remove_dup(original)

print("Original list: ", original)
print("Removed duplicates: ", removed)'''


'''def remove_duplicates(user_list):
    unique_list = []

    for elements in user_list:
        if elements not in unique_list:
            unique_list.append(elements)
    return unique_list

user_given = input("enter list: ")
original = [int(x) for x in user_given.split()]

print(remove_duplicates(original))
'''

'''class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def measure(self):
        print(f"The area is {self.length*self.width} sq units.")

instance = Rectangle(12,2).measure()
'''

'''class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} who is {self.age} years of age says woof!")

my_dog = Dog("Buddy", 3)
my_dog.bark()  # Output: Buddy says woof!'''


'''class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def status(self):
        if self.grade > 80:
            print(f"{self.name} has Passed")
        else:
            print(f"{self.name} has Failed")

S1 = Student("Alim", 79).status()
S2 = Student("Taqi", 82).status()'''


'''def set_int(set1, set2):
    return set1 & set2

print(set_int({1,2,3,4},{1,2,3,4,5}))
'''

'''def swat_tuple(t):
    return (t[2], t[1], t[0])

print(swat_tuple((1,2,3)))'''

'''def tts(t):
    return ''.join(t)

print(tts(('h', 'e', 'l', 'l', 'o')))'''


'''def new_dict(list1, list2):

    return dict(zip(list1,list2))

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

print(new_dict(list1, list2))'''


'''def freq(string):
    fre = {}

    for characters in string:
        if characters in fre:
            fre[characters] += 1

        else:
            fre[characters] = 1

    return fre

print(freq("Excellentttoss"))'''

'''def max_val(given_list):

    maximum = float('-inf')

    for elements in given_list:
        if elements > maximum:
            maximum = elements

    return maximum

print(max_val([1,2,6,3,4,5]))


def max_val(given_list):

    minimum = float('inf')

    for elements in given_list:
        if elements < minimum:
            minimum = elements

    return minimum

print(max_val([2,6,1,3,4,5]))'''


#1. Lambda Function to handle data req:

# integration


'''def calculate_monthly_budget():
    # Input monthly income
    monthly_income = float(input("Enter your monthly income: "))
    
    # Input fixed expenses
    fixed_expenses = []
    n = int(input("Enter the number of fixed expenses: "))
    for i in range(n):
        expense = float(input(f"Enter fixed expense {i+1}: "))
        fixed_expenses.append(expense)
    
    # Calculate total fixed expenses
    total_fixed_expenses = sum(fixed_expenses)
    
    # Input variable expenses
    variable_expenses = []
    m = int(input("Enter the number of variable expenses: "))
    for i in range(m):
        expense = float(input(f"Enter variable expense {i+1}: "))
        variable_expenses.append(expense)
    
    # Calculate total variable expenses
    total_variable_expenses = sum(variable_expenses)
    
    # Calculate remaining budget
    remaining_budget = monthly_income - total_fixed_expenses - total_variable_expenses
    
    # Conditional selection for different scenarios
    if remaining_budget > 0:
        print(f"Your remaining budget is Tk {remaining_budget:.2f}. You are within your budget.")
    elif remaining_budget == 0:
        print("Your budget is exactly balanced.")
    else:
        print(f"Your remaining budget is Tk {remaining_budget:.2f}. You have exceeded your budget.")
        
calculate_monthly_budget()
'''


#leetcode fibonacci
'''class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.fib[n-2] + self.fib[n-1]

print(Solution.fib(3))
'''

'''class Person:

    def __init__(self, name, age, location, relationship, education):
        self.name = name
        self.age = age
        self.location = location
        self.relationship = relationship 
        self.education = education 

attendee_1 = Person("John", 27, "Boston", "Single", "Married")
print("Relationship status of the person is: ", attendee_1.relationship)
print("Name and age of the attendee: ", attendee_1.name, attendee_1.age)
'''

'''
Problem:
A cab service offers three types of passes. 1D, 7D, 30D. 
A T days pass can be used for a continuous duration only. 

Consider the days of the year being labeled sequentially from 1 to 365. 
Travelling is required only on some selected days of the year(input). 

Given the cost of different passes and the days on which travel is required, 
Calculate the minimum amount using which we can travel on all these days.

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11(2 + 7 + 2)
'''

#global interpreter
#shellp cpy and deep copy
#mutable and immutable
#unit test  



'''def mincostTickets(days, costs):
    # Set to quickly find the days we need to travel on
    travel_days = set(days)
    
    # DP array to store the minimum cost up to each day
    dp = [0] * 366  # for days from 1 to 365
    
    for i in range(1, 366):
        if i not in travel_days:
            # If we don't need to travel on this day, inherit the cost from the previous day
            dp[i] = dp[i - 1]
        else:
            # Calculate the minimum cost by choosing between 1-day, 7-day, and 30-day passes
            dp[i] = min(
                dp[i - 1] + costs[0],  # 1-day pass
                dp[i - 7] + costs[1] if i >= 7 else costs[1],  # 7-day pass
                dp[i - 30] + costs[2] if i >= 30 else costs[2]  # 30-day pass
            )
    
    # The minimum cost to cover all travel days is now in dp[365]
    return dp[365]

# Example usage:
days = [1, 4, 6, 7, 8, 20]
costs = [2, 8, 15]
print(mincostTickets(days, costs))  # Output: 11'''



'''user_list = [1.2, 3, 2, 4, 2]

total = 0

for numbers in user_list:

    total += numbers

print("The sum of given numbers is", total)
'''

'''user_list = [1, 2, 3, 4, 5]

reversed = []

for numbers in user_list:

    reversed = user_list[::-1]

print("The reversed list is", reversed)

'''


'''user_input = input("Enter a list of numbers: ")
user_list  = [int(x) for x in user_input.split(',')]
print("User entered: ", user_list)

reversed_list = []

for elements in user_list:
    sorted_list = user_list[::-1]


print("Reversed list: ", reversed_list)'''

'''user_input = input("Enter a list of numbers: ")
user_list  = [int(x) for x in user_input.split(',')]
print("User entered: ", user_list)

reversed_list = []

for elements in user_list:
    sorted_list = sorted(user_list)


print("Reversed list: ", sorted_list)'''