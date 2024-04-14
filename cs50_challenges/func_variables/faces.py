def convert(input_string):
    new_string = input_string.replace(":)", "🙂").replace("(:", "🙁")
    return new_string

def main():
    the_string = str(input("Enter your mood "))
    converted_string = convert(the_string)
    print(converted_string)

if __name__ == "__main__":
    main()