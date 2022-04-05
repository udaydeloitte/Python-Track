rows=int(input("Enter no of rows: "))
for i in range(rows):
    print(" "*(rows-i-1),end="")
    print("* ",end='')
    if i>=1:
        print(" "*(2*i-1),end='')
        print("*",end='')
    print()
print("* "*(rows+1))

print()
#ques 2b
for i in range (rows):
    for j in range (rows):
        if i==0 or j==(rows-1) or i==j:
            print('*', end='')
        else:
            print(end=" ")
    print()