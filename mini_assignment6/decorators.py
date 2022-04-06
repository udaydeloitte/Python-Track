#write a decorator which will take a function and execute it twice.
print("Enter values of num1 and num2: ")
lst = list(map(int,input().split()))
num1 = lst[0]
num2 = lst[1]

def multiply(func):
    def inner(num1,num2):
        func(num1,num2)
        return func(num1,num2)
    return inner

@multiply
def executableFunc(num1,num2):
    print(num1*num2)

executableFunc(num1,num2)
print()

#Create a generator to return the Fibonacci sequence starting from the first element

input_=int(input("Enter number for Fibonacci sequence: "))
def fib(n):
    x, y = 0, 1
    for i in range(n):
        yield x
        x, y = y, x+y
print(list(fib(input_)))
