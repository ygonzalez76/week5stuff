#collections = single "variable" used to store multiple values
#list = [] ordered and changeable. Duplicates OK
#set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#tuple = () ordered and unchangable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut", "pineapple", "kiwi", "papaya", "strawberry"]
# print(fruits[::2]) #gives every second element
# print(fruits[::-1]) #gives you the elements backwards

# #print(fruits[0])
# for fruit in fruits:
#     print(fruit)

# print(dir(fruits)) #dir gives you all the attributes of a list, what it can do
# print(help(fruits)) #gives you helpful documentation
# print(len(fruits)) #len gives you the length of it

# print("mango" in fruits) #tells you if its in the list
# fruits[0] = "coconut" 
# fruits.append("pineapple") #adds to the end of your list
# fruits.remove("apple") #speaks for itself
# fruits.insert(0,"pineapple") #put something there and push everything over
# fruits.sort() #puts everything in alphabetical order
# fruits.reverse() #speaks for itself
# fruits.clear() #removes everything
print(fruits.index("apple"))

print(fruits)
