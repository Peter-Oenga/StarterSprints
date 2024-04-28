def pow(a, b):
    answer = a
    if b == 0:
        return 1
    elif b < 0:
        for i in range(-b-1):
            answer *= a
        return 1 / answer 

    else:
        for i in range(b-1):
         answer *= a
        
        
        return answer

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(5, -3))
print(pow(-4, 5))

