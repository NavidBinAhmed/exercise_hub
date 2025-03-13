# tuple: tah-pol
tpl = ()
print(type(tpl))

'''tuples are immutable, it does not have add, remove, etc methods, list does'''
'''uses () and list [] '''
'''tuples' operations  are faster than list because of immutability'''
tpl1= (1,2,3,4, 'hello')
print(tpl1)


# set and dictionary are designed using one common data structure: 
# which is hashing
# this DS's lookup or searching time is constant: O(1)
'''sets are not ordered - we can not use index to call an eleemnt, lists are ordered'''
'''sets do not use duplicates, lists do'''
'''uses curly braces {}'''
'''index number is unique for a particluar element'''
'''can not call element using the index number (like tuple, list or dict)'''
'''set1[0] in below code - showing TypeError''' 

set1 = {1,2,3,2,4}
print(set1)   

# dictionary
'''dictionary uses curly braces, and key:value pair'''
'''key is unique not allowing duplicates like a sets' element'''
'''we are entering the manual index number by ourselves as the key (name)'''
'''in set index number is the key'''
'''common thing is both uses hashmaps'''
'''dictionary is mutable, as we see below BD is replaced by USA'''
dict1 ={'key': 'value', 'nationality': ''}
print(dict1)
print(type(dict1))

dictionary = {'name': 'navid', 'place': 'BD', 'email': 'navid@yahoo.com'}
print(dictionary)
print(dictionary['email'])
print(dictionary['place'])
dictionary['place'] = 'USA'
print(dictionary)


# string
'''string is mutable'''
'''accessible using indexing- only sets can't be accessed using index numbers'''
'''uses inverted: "" or '' to express'''
'''below are some operations in string'''
my_string = 'I am Navid'
print(my_string)

first_char = my_string[0]
second_char = my_string[-1]
print(first_char)
print(second_char)

substring = my_string[0:4] # outputs: I am
print(substring)
print(len(my_string))

greeting = "Hello!"
full_string = greeting + ' ' + my_string + '.'
print(full_string)

my_s_u = my_string.upper()
my_s_l = my_string.lower()
print(my_s_u)
print(my_s_l)

replaced_string = my_string.replace("I am", "He is")
print(replaced_string)

index_finding = my_string.find('Navid')
print(index_finding)

new_string = 'Hello, I am Navid, He is Akash.'
words = new_string.split(',')
print(words)
joined_string = '-'.join(words)
print(joined_string)

contained_word = "Akash" in new_string
print(contained_word)

string = "Navid"
for char in string:
    print(char, end = ',')
print() # for a new line