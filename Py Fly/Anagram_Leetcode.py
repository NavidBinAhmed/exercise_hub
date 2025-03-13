class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        # Convert both strings to lowercase
        str1 = str1.lower()
        str2 = str2.lower()

        # Early return if lengths differ
        if len(str1) != len(str2):
            return False

        char_count = {}

        # Count characters in the first string
        for char in str1:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Decrease the count for the second string
        for char in str2:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] < 0:
                    return False
            else:
                return False

        return True






#alternative solution : Leetcode not accepted, but used ASCII character conversion for upper and lower case characters
'''def Anagram(str1, str2):
    dict = {}
    for i in range(len(str1)):
        if ord(str1[i]) <= 122 and ord(str1[i]) >= 97:
            if ord(str1[i]) - 32 not in dict:
                dict[ord(str1[i]) - 32] = 1
            else:
                dict[ord(str1[i]) - 32] = dict[ord(str1[i]) - 32] +1
        else:
            if ord(str1[i]) not in dict:
                dict[ord(str1[i])] = 1
            else:
                dict[ord(str1[i])] = dict[ord(str1[i])] +1


    for i in range(len(str2)):
        if ord(str2[i]) <= 122 and ord(str2[i]) >= 97:
            if ord(str2[i]) - 32 in dict:
                if dict[ord(str2[i]) - 32] != 0:
                    dict[ord(str2[i]) - 32] = dict[ord(str2[i]) - 32] -1
                else:
                    return 0      
            else:
                return 0
        else:
            if ord(str2[i]) in dict:
                if dict[ord(str2[i])] != 0:
                    dict[ord(str2[i])] = dict[ord(str2[i])] -1
                else:
                    return 0
            else:
                return 0
    return 1


str1 = input("Enter str1: ")
str2 = input("Enter str2: ")

if Anagram(str1, str2):
    print("Yes")
else:
    print("No")'''
    
