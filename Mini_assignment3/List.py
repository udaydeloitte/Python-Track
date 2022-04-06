from collections import Counter
#Return all the duplicate values from list of arraylist
print("Return all the duplicate values from list of arraylist: ")
arr = [ [1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4] ]
for i in arr:
    d=dict(Counter(i))
    for j in d:
        if d[j]>1:
            print(j,"->",d[j],end=" ")
    print()
print()

print("Merge two lists: ")
merge=[]
list1=["Hello", "take"]
list2=["Dear","Sir"]
for i in list1:
    for j in list2:
        merge.append(i+" "+j)
print(merge)
print()
# Given a nested list extend it by adding the sub list["h", "i", "j"]in such a way that it will look like the following list
print("Extend list")
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
print(list1)