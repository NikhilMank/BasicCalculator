import math

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b, ans=None):
    if b==0:
        print("Cannot divide by zero!!!!!! Please enter valid calculations!!!!!!")
        return ans
    else:
        return a/b

def mod(a,b):
    return a % b

def exp(a,b):
    return a ** b

def floor_div(a,b):
    return a // b

def sqrt(a):
    return a ** 0.5

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def power(a, b):
    return a ** b

def absolute(a):
    return abs(a)

def log(a, base=10):
    return math.log(a, base)

def sin(angle):
    return math.sin(math.radians(angle))

def cos(angle):
    return math.cos(math.radians(angle))

def tan(angle):
    return math.tan(math.radians(angle))

def asin(value):
    return math.degrees(math.asin(value))

def acos(value):
    return math.degrees(math.acos(value))   

def atan(value):
    return math.degrees(math.atan(value))

def radians(degrees):
    return math.radians(degrees)

def degrees(radians):
    return math.degrees(radians)

def help():
    print("Example usage:")
    print(f"{add(5, 3)=}")
    print(f"{sub(5, 3)=}")
    print(f"{mul(5, 3)=}")
    print(f"{div(5, 3)=}")
    print(f"{mod(5, 3)=}")
    print(f"{exp(5, 3)=}")
    print(f"{floor_div(5, 3)=}")
    print(f"{sqrt(25)=}")
    print(f"{factorial(5)=}")
    print(f"{power(2, 3)=}")
    print(f"{absolute(-5)=}")
    print(f"{log(100)=}")
    print(f"{sin(30)=}")
    print(f"{cos(60)=}")
    print(f"{tan(45)=}")
    print(f"{asin(0.5)=}")
    print(f"{acos(0.5)=}")
    print(f"{atan(1)=}")
    print(f"{radians(180)=}")
    print(f"{degrees(math.pi)=}")
    print("End of example usage.")