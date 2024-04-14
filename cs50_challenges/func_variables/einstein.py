speed_of_light = 300000000 * 300000000 

def calculate_Energy(mass):
    Energy = mass * speed_of_light
    return Energy

def main():
    #Take the user's input
    mass = int(input("Input the mass(kg): "))

    # Call the function to calculate the energy
    Result = calculate_Energy(mass)
    print(Result)

if __name__ == "__main__":
    main()
