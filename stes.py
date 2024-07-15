#sets ezgersizi 
fruits = {"orange", "apple", "cherry"}
#print(fruits[0]) indekslenemez
for x in fruits :
    print(x)
fruits.add("banana")
fruits.add("kiwi")
fruits.update(["melon", "grape"])
fruits.remove("melon")
fruits.discard("apple")
print(fruits)
fruits.pop()

myList= [1,2,3,4,4,3,2,1]
print(myList)
print(set(myList))