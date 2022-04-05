from itertools import permutations
from collections import Counter
class Stringclass:
    def __init__(self,inp):
        self.string=inp
    def printlength(self):
        return len(self.string)
    def converttolist(self):
        return list(self.string)
1
class Pairpossible(Stringclass):

    def pair(self):
        self.perm=permutations(list(self.string))
        li=[]
        for i in self.perm:
            li.append(i)
            print(list(i), end=" ")
    def show(self):
        return self.li



class SearchCommonElements(Stringclass):
    def commonele(self):
        d=dict(Counter(list(self.string)))
        ans=[]
        for j in d:
            if d[j]>=2:
                ans.append(j)
        return ans







userinput=input()
objstringclass=Stringclass(userinput)
print("Length of string is: ",objstringclass.printlength())
print("String converted to list: ",objstringclass.converttolist())
objpairpossible=Pairpossible(userinput)
print("All possible pairs are: ")
objpairpossible.pair()
objsearchcommonelements=SearchCommonElements(userinput)
print()
print("Common elements are: ",objsearchcommonelements.commonele())









