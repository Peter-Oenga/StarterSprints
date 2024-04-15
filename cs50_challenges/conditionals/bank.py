greeting = input("Greeting: ")

if greeting == "hello".lower():
    print("$0")
elif greeting[0] == "h".lower():
    print("$20")
else:
    print("$100")