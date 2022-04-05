#Map the dictionary in the following manner
print("Map the dictionary in the following manner: ")
Keys = ["Ten", "Twenty", "Thirty"]
values=[10, 20, 30]
dictinoary={}
for key in range(len(Keys)):
    dictinoary[Keys[key]]=values[key]
print(dictinoary)


#Merge following two Python dictionaries into one
print("Merge following two Python dictionaries into one: ")
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 33, 'Fourty': 40, 'Fifty': 50}
for i in dict2:
    if i in dict1:
        dict1[i]=dict2[i]
    else:
        dict1[i]=dict2[i]
print(dict1)
print()

#Rename key city to location in the following dictionary
print("Rename key city to location in the following dictionary: ")
sampleDict = {

  "name": "Kelly",

  "age":25,

  "salary": 8000,

  "city": "New york"

}
value=sampleDict["city"]
del sampleDict["city"]
sampleDict["location"]=value
print(sampleDict)
print()


#Convert Dictionary to list
print("Convert Dictionary to list: ")
dict1={"HuEx": [1, 3, 4], "is": [7, 6], "best": [4, 5]}
temp=[]
j=0
for i in dict1:
    temp.append(dict1[i])
    temp[j].insert(0,i)
    j+=1
print(temp)