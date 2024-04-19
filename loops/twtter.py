input_str = input("Input: ")

vowels = ["a", "e", "i", "o", "u"]
for vowel in vowels:
    input_str = input_str.replace(vowel, "")
print(input_str)

