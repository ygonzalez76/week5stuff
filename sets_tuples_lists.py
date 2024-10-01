#collections = single "variable" used to store multiple values
#list = [] ordered and changeable. Duplicates OK
#set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# #tuple = () ordered and unchangable. Duplicates OK. FASTER

# fruits = ["apple", "orange", "banana", "coconut", "pineapple", "kiwi", "papaya", "strawberry"]
# # print(fruits[::2]) #gives every second element
# # print(fruits[::-1]) #gives you the elements backwards

# # # #print(fruits[0])
# # for fruit in fruits:
# #     print(fruit)

# # print(dir(fruits)) #dir gives you all the attributes of a list, what it can do
# # print(help(fruits)) #gives you helpful documentation
# # print(len(fruits)) #len gives you the length of it

# # print("mango" in fruits) #tells you if its in the list
# # fruits[0] = "coconut" 
# # fruits.append("pineapple") #adds to the end of your list
# # fruits.remove("apple") #speaks for itself
# # fruits.insert(0,"pineapple") #put something there and push everything over
# # # fruits.sort() #puts everything in alphabetical order
# # # # fruits.reverse() #speaks for itself
# # # # fruits.clear() #removes everything
# # # print(fruits.index("apple"))

# # # print(fruits)

# # cars = ["ford", "volvo", "BMW"]
# # #add 4 new cars in the list
# # print(cars.append("Honda"))
# # print(cars.append("Trax"))
# # print(cars.append("Murano"))
# # print(cars.append("Cadilac"))
# # #print out the list of cars in an f-string
# # #that says "The cars in the list are: "
# # print(f"The cars in this list are: {cars}")
# # #replace the last element in the list with another car
# # cars[-1] = "austin martin"
# # #print out the list of cars in an f-string
# # print(f"The cars in this list are: {cars}")
# # #replace the third element in the list with another car
# # #print out the list of cars in an f-string
# # cars[2] = "Tesla"
# # print(f"The cars in this list are: {cars}")
# # #insert a new car in the 2nd position
# # #print out the list of cars in an f-string
# # cars.insert(1,"Toyota")
# # print(f"The cars in this list are: {cars}")
# # #remove the third element from the list
# # #print out the list of cars in an f-string
# # cars.remove("volvo")
# # print(f"The cars in this list are: {cars}")
# # #check if the list contains the car "Ford"
# # #print out the result in an f-string
# # print("Ford" in cars)
# # print(f"The cars in this list are: {cars}")

# # for car in cars:
# #     requestCar = input("Enter a car: ")
# #     cars.append(requestCar)
# #     print(f'The cars in this list are: {cars}')
# #     if len(cars) > 10:
# #         print("You have reached the maximum number of cars.")
# #         break

# # #challenge
# # Step 1: Create a list of friends
# friends = ["Alice", "Bob", "Charlie"]

# # Step 2: Add 4 new friends to the list
# friends.extend(["David", "Eva", "Frank", "Grace"])

# # Step 3: Print the list of friends using f-string
# print(f"List of friends: {friends}")

# # Step 4: Replace the last element with another friend
# friends[-1] = "Hannah"

# # Step 5: Print the updated list of friends using f-string
# print(f"Updated list of friends (after replacing last friend): {friends}")

# # Step 6: Replace the third element with another friend
# friends[2] = "Irene"

# # Step 7: Print the updated list of friends using f-string
# print(f"Updated list of friends (after replacing third friend): {friends}")

# # Step 8: Insert a new friend in the second position
# friends.insert(1, "Jack")

# # Step 9: Print the final list of friends using f-string
# print(f"Final list of friends: {friends}")

# #####################sets###############################
#sets are unordered and unindexed
#they are defined using curly brackets
#they do not allow duplicates
fruits = {"apple", "banana", "mango", "cherry", "watermelon"}
print(fruits)
# print(dir(fruits)) #attributes can be used with sets
# print(help(fruits)) #documentation/methods that can be used with set 
# print(len(fruits)) #number of elements in the set
# print("volvo" in fruits) #check if an element is in the set
#add an element to the set
print(fruits.add("orange"))
print(fruits)
print(fruits.add("kiwi"))
print(fruits)
#add multiple elements to the set
print(fruits.update(["orange", "kiwi", "pineapple"]))
print(fruits)
#remove an element from the set
print(fruits.remove("banana"))
print(fruits)
print(fruits.pop()) #removes the last element in trhe set
print(fruits)
print(fruits.clear()) #clears the set
print(fruits)
#when do you want to use sets?
#sets are useful when you want to store a 
#collection of items that should not be changed,
#and you do not care about the order of the items.
#example: a collection of unique items
social_security_numbers = {123456789, 987654321, 123456789}
#remove the last element in this set
print(social_security_numbers.pop())
#add another social security number
print(social_security_numbers.add(345678901))
print(social_security_numbers)
social_security_numbers.add(123456789)
print(social_security_numbers)

#############tuples##################
# #tuples are immutable and are defined using parenthesis
# #create a tuple called my_tuple with the following values:
example_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(example_tuple)
# print(example_tuple.count(2)) #count the number of times
# #the value 2 appears in the tuple
# print(dir(example_tuple)) #attributes that can be used with tuples
# print(help(example_tuple)) #documentation/methods that can be used with tuples
# print(len(example_tuple)) #number of elements in the tuple
# print(2 in example_tuple) #check if an elemtn is in the tuple
# #if you want to find the index pf a value in a tuple 
# print(example_tuple.index(2))
# lymeric = "peter pipe picked a peck of pickled peppers peppers"
# #convert the string to a tuple
# #split it first
# lymeric_tuple = tuple(lymeric.split())
# print(lymeric_tuple)
# #find how mamy times the word "peck" appears in the tuple
# print(lymeric_tuple.count())

#loops with tuples
for item in example_tuple:
    print(item)

#########dictionary###########
#dictionaries are unordered, changeable and indexed
    #they are defined using curly brackets
    #they have keys and values
#a collection of {key:value} pairs, no duplicates
#keys are unique
#values can be of any data type
capitals = {"Kenya":"Nairobi",
            "Uganda": "Kampala",
            "Tanzania": "Dodoma",
            "Rwanda" : "Kigali",
            "China" : "Beijing"
            "USA" : "Washington DC"}
print(capitals)
print(dir(capitals)) #attributes that can be used with dictionaries
print(help(capitals)) #documentation/methods that can be used with dictionaries
print(len(capitals)) #number of items in the dictionary
#if you want to check the value of a key in the dictionary
print(capitals["Kenya"])
print(capitals.get("Kenya"))
#add an item to the dictionary
capitals["South Africa"] = "Pretoria"
print(capitals)
capitals.update("Nigeria":"Abuja")
#add three more countries and their capitals to the dictionary
capitals.update({"France" : "Paris", "Germany" : "Berlin", "Italy": "Rome"})
capitals.pop("China") #remove an item from the dictionary
print(capitals)
#clear the dictionary
#capitals.clear() #do not run this
#loop through the dictionary to get the keys
for key in capitals:
    print(f"these are the {key}")

#print the values in the dictionary
for value in capitals.values():
    print(value)

#print the key value pairs in the dictionary
items_all = capitals.items() #key value pairs
for key, value in items_all:
    print(f"{key} is the capital of {value}")