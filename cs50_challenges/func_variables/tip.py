def main():
    amount = dollars_to_float(input("What  is the amount of the food: "))
    percentage = percent_to_float(input("What percentage would you like to tip: "))
    tip = amount * percentage
    print(f"${tip:.2f}")

def dollars_to_float(d):
    result = d.replace("$", " ")
    return float(result)

def percent_to_float(w):
    w = w.replace("%", " ")
    return float(w) / 100

main()