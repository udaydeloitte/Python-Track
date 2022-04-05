from itertools import permutations
from collections import Counter
class Stringclass:
    def __init__(self,inp):
        self.string=inp
    def printlength(self):
        return len(self.string)
    def converttolist(self):
        return list(self.string)

class Pairpossible(Stringclass):

    def pair(self):
        self.perm=permutations(list(self.string))
        li=[]
        for i in self.perm:
            li.append(list(i))
        return li
    def common(self):
        pairinput=input()
        oplist=[]
        d=dict(Counter(pairinput))
        for j in set(self.string):
            if j in d:
                oplist.append(j)
        return oplist
class SearchCommonElements(Pairpossible):
    def commonele(self):
        var=super().common()
        return var

class EqualSumPairs(SearchCommonElements):
    def call(self):
        cnt=super().pair()
        ansd=dict()

        for i in cnt:
            add=0
            for k in i:
                add+=int(k)
            if add not in ansd:
                ansd[add]=0

            else:
                del ansd[add]
        lis=[]
        for i in cnt:
            add=0
            for k in i:
                add+=int(k)
            if add in ansd:
                lis.append(i)
        return lis






userinput=input()
objstringclass=Stringclass(userinput)
print("Length of string is: ",objstringclass.printlength())
print("String converted to list: ",objstringclass.converttolist())
objpairpossible=Pairpossible(userinput)
print("All possible pairs are: ")
print(objpairpossible.pair())
objsearchcommonelements=SearchCommonElements(userinput)
print()
print("common elements are: ",objsearchcommonelements.commonele())
objEq=EqualSumPairs(userinput)
print(objEq.call())










