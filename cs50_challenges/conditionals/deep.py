import re

answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# answer = " ".join(re.split(r'\s+', answer)).lower()
# answer = " ".join(answer.split()).lower()
answer = " ".join(re.split(r'\s+', answer.strip())).lower()

if answer == 42:
    print("Yes")

elif answer == "forty-two":
    print("Yes")
elif answer == "forty two":
    print("Yes")
else:
    print("No")