#Using a lambda function take inputs as 4 integers and give the output for equation

lst=list(map(int,input("Enter values of a, b, c and x: ").split()))
a,b,c,x=lst[0],lst[1],lst[2],lst[3]

#calculating the value of expression
output= lambda a,b,c,x: a*(x*x)+b*x+c

print(output(a,b,c,x))
print()

#Using map() function and lambda and count() function create a list consisted of the number of occurence of both letters: A and a.

lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

#count for A
out_putForA=list(map(lambda n:n.count("A"),lst1))
print("count of A: ",out_putForA)

#counting for a
out_putFora=list(map(lambda n:n.count("a"),lst1))
print("count of a: ",out_putFora)
