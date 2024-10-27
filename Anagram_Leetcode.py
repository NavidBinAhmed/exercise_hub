def Anagram(str1, str2):
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
    print("No")
    