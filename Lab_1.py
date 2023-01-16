print("ADDITION OF TWO NUMBERS \n")
a=input("Enter no 1:")
a=int(a)
b=input("Enter no 2:")
b=int(b)
print("Sum of the numbers is: ",a+b)
print("SECOND LARGEST NUMBER \n")
arr=[]
n=int(input("Number of elements in array:"))
print("Enter the elements of the array : ")
for i in range(0,n):
   num=int(input())
   arr.append(num)

arr.sort()
print("The second largest number is : ",arr[n-2])
print("FACTORIAL OF A NUMBER \n")
a=input("Enter a number : ")
a=int(a)
def factorial(num):
    if (num==0):
        return 1
    else:
        fact=num*factorial(num-1)
        return fact

print("The factorial of the number is: ",factorial(a))
print("\n")
print("PATTERN 1")
n=int(input("Enter a number  : "))
print("The pattern is : ")
def pattern(n):
    k = 2 * n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k - 2
        for j in range(0,i+1):
            print("* ", end="")
        print("")

pattern(n)
print("\n")
print("PATTERN 2")
n=int(input("Enter a number  : "))
print("The pattern is : ")
for i in range(0, n):
    for j in range(0, i+1):
        print("* ", end="")
    print("")
