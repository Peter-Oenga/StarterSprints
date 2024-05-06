"""
Write a python function to calculate the temperature in fahrneit
"""
def farhneit(T):
    return ((float(9) / 5 * T + 32))

def celcius(T):
    return (float(5)/9) * (T-32)

temperatures = (36.5, 37, 37.5, 38, 39)

F = map(farhneit, temperatures)
C = map(celcius, F)

print(list(F))

print(list(C))