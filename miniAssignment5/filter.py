# Convert a number to positive if it's negative in the list. Only pass those that are converted
# from negative to positive to the new list.
# input =[-1000, 500, -600, 700, 5000, -90000, -17500]
import functools

output_filter = list(map(abs,list(filter(lambda n: n if (n < 0) else None, list(map(int, input("Enter list of numbers: ").split()))))))
print(output_filter)
print()

# Take the first two values, run the function on them. Then take the result and the next value and
# have a multiplication between them. etc. When no more values are left, return the last result.
print("Implementing reduce function: ")
lst1 = [-10, 5, -6, 7, 50, -90, -1]
output_reduce = functools.reduce(lambda x, y: x * y, lst1)
print(output_reduce)
print()

# Using zip and dict functions create a dictionary which has its key-value pairs coming from lst1 and lst2.
print("Implementing zip function: ")
keys = ["Netflix", "Hulu", "Sling", "Hbo"]
values = [198, 166, 237, 125]
output_dictionary = dict(zip(keys, values))
print(output_dictionary)
