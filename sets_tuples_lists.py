#collections = single "variable" used to store multiple values
#list = [] ordered and changeable. Duplicates OK
#set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# #tuple = () ordered and unchangable. Duplicates OK. FASTER

# fruits = ["apple", "orange", "banana", "coconut", "pineapple", "kiwi", "papaya", "strawberry"]
# # print(fruits[::2]) #gives every second element
# # print(fruits[::-1]) #gives you the elements backwards

# # #print(fruits[0])
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
# # fruits.sort() #puts everything in alphabetical order
# # # fruits.reverse() #speaks for itself
# # # fruits.clear() #removes everything
# # print(fruits.index("apple"))

# # print(fruits)

# cars = ["ford", "volvo", "BMW"]
# #add 4 new cars in the list
# print(cars.append("Honda"))
# print(cars.append("Trax"))
# print(cars.append("Murano"))
# print(cars.append("Cadilac"))
# #print out the list of cars in an f-string
# #that says "The cars in the list are: "
# print(f"The cars in this list are: {cars}")
# #replace the last element in the list with another car
# cars[-1] = "austin martin"
# #print out the list of cars in an f-string
# print(f"The cars in this list are: {cars}")
# #replace the third element in the list with another car
# #print out the list of cars in an f-string
# cars[2] = "Tesla"
# print(f"The cars in this list are: {cars}")
# #insert a new car in the 2nd position
# #print out the list of cars in an f-string
# cars.insert(1,"Toyota")
# print(f"The cars in this list are: {cars}")
# #remove the third element from the list
# #print out the list of cars in an f-string
# cars.remove("volvo")
# print(f"The cars in this list are: {cars}")
# #check if the list contains the car "Ford"
# #print out the result in an f-string
# print("Ford" in cars)
# print(f"The cars in this list are: {cars}")

# for car in cars:
#     requestCar = input("Enter a car: ")
#     cars.append(requestCar)
#     print(f'The cars in this list are: {cars}')
#     if len(cars) > 10:
#         print("You have reached the maximum number of cars.")
#         break

# #challenge
# Step 1: Create a list of friends
friends = ["Alice", "Bob", "Charlie"]

# Step 2: Add 4 new friends to the list
friends.extend(["David", "Eva", "Frank", "Grace"])

# Step 3: Print the list of friends using f-string
print(f"List of friends: {friends}")

# Step 4: Replace the last element with another friend
friends[-1] = "Hannah"

# Step 5: Print the updated list of friends using f-string
print(f"Updated list of friends (after replacing last friend): {friends}")

# Step 6: Replace the third element with another friend
friends[2] = "Irene"

# Step 7: Print the updated list of friends using f-string
print(f"Updated list of friends (after replacing third friend): {friends}")

# Step 8: Insert a new friend in the second position
friends.insert(1, "Jack")

# Step 9: Print the final list of friends using f-string
print(f"Final list of friends: {friends}")