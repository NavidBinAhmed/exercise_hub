# function definition
def check_pallindrome(string):
    string = string.lower().replace(" ","")
    return string==string[::-1]

# driver code
string = "A man a plan a canal panama"
# function calling
result = check_pallindrome(string)
print(result)

# driver code
string_2 = "madam"
# function calling
result_2 = check_pallindrome(string_2)
print(result_2)

# driver code
string_3 = "Hi Navid"
# function calling
result_3 = check_pallindrome(string_3)
print(result_3)