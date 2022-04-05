
#Diamond Pattern
rows=int(input("Enter no of rows: "))
for i in range(rows):
    print(" "*(rows-i-1)+"*"*(2*(i+1)-1))
for i in range(rows-1):
    print(" "*(i+1)+"*"*(2*(rows-i-1)-1))

print()

for i in range(rows):
    print(" "*(rows-i-1),end="")
    print("* ",end='')
    if i>=1:
        print(" "*(2*i-1),end='')
        print("*",end='')
    print()
print("* "*(rows+1))

print()

for i in range (rows):
    for j in range (rows):
        if i==0 or j==(rows-1) or i==j:
            print('*', end='')
        else:
            print(end=" ")
    print()

# pascal triangle
def printPascal(n: int):
    arr = [[0 for x in range(n)]
           for y in range(n)]

    for line in range(0, n):

        for i in range(0, n):

            if i is 0 or i is line:
                arr[line][i] = 1
                print(arr[line][i], end=" ")


            else:
                arr[line][i] = (arr[line - 1][i - 1] +
                                arr[line - 1][i])
                print(arr[line][i], end=" ")
        print("\n", end="")
n=int(input("Enter no of rows: "))
printPascal(n)