str1 = input("Enter String 1 ")
str2 = input("Enter String 2 ")

if len(str1) != len(str2):
    print("Not Anagrams")
else:
    if sorted(str1) == sorted(str2):
        print(str1 , "and", str2, "Are anagrams")
    else:
        print("Not anagrams")