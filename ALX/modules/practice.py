import sys

def fib(n):
    result = []
    a, b = 0, 1
    

    while a < n:
        result.append(a)
        
        a , b = b , a + b

    return result

def fib1(n):
    a, b = 0, 1

    while a < n :
        print(a, end="")

        a, b = b, a + b

    print()

if __name__ == "__main__":
    limit = int(sys.argv[1])
    fib(limit)