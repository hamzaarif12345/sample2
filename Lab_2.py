import math
# ARITHMETIC FUNCTIONS
print("ARITHMETIC FUNCTIONS")
num=int(input("Enter a number: "))
print('The floor value is:', math.floor(num))
print('The square root is:', math.sqrt(num))
print('The ceiling value is:', math.ceil(num))
print('The absolute value is:', math.fabs(num))
print('Modulus operation: ',math.fmod(num,10))
a=int(input("Enter the first no : "))
b=int(input("Enter the second no : "))
print('The GCD of a and b is: ' + str(math.gcd(a, b)))
# LOGARITHMIC AND EXPONENTIAL
print("\n")
print("LOGARITHMIC AND EXPONENTIAL FUNCTION")
print("The log2 of 32 is:", math.log2(32))
print("The log 2 with base 10 is:", math.log(2,10))
print("Logarithm (1+x) value of 10 is:", math.log1p(10))
print("math.log(18.98):", math.log(18.98))
print("math.log(math.pi):", math.log(math.pi))
print('e^x (using function exp()) is:', math.exp(num)-1)
print('e^x (using function expml()) is:', math.expm1(num))
print("\n")
print("EXPRESSING NUMBERS IN THE EXPONENTIAL FORMAT")
no_int=int(input("Enter an integer: "))
print(math.exp(no_int))
no_negative_int=int(input("Enter a negative integer: "))
print(math.exp(no_negative_int))
no_float=float(input("Enter an float value: "))
print(math.exp(no_float))
print("\n")
print("VALUE OF PI ")
print("The value of pi is : ",math.pi)
