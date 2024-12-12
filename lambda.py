# Lambda Function: using an anonymous function without declaring a function
'''expression'''
# variable = lambda arguments: expression 

expression = lambda a,b,c : a+b-c
print(expression(5,5,2))

# function calling
result = expression(4,4,2)
print(result)

# driver code
a,b,c = 2,2,1
result = expression(a,b,c)
print(result)

function = lambda a,b:a*b
print(function(2,3))