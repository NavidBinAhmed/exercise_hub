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
set1 = {1,2,3,2,4}
print(set1) 


'''dictionary uses curly braces, and key:value pair'''
'''key is unique not allowing duplicates like a sets' element'''

dict1 ={'key': 'value'}
print(dict1)
print(type(dict1))