# Repitition Statements
# Data types allowed to be interated: Lists, Ranges, Sets, Tuple, Dictionaries, Strings

# x = range(5,11)
petName = ["snowy", "blacky", "bruno"]

# for loop
# for(initialization;condition; incrementation/decre) - JAVA

# for num in x:
#     print(num)

# Slicing a lists
for name in petName[2:0:-1]:
    print(name) 

# reverse -> use -1

 # Looping Dictionaries
 # key: value
# user= {
#     "first_name" : "Johhnyte",
#     "last_name" : "Napoles",
#     "age" : 32,
#     "average" : 81.76, 
#     "list_subjects" : ["Programming", "Mathematics", "English"]


# crtl + / - shortcut for comment

# for key in user:
#     print(key, ":", user[key])

# Looping List of Dictionaries
# list_of_users = [
#     {
#     "first_name" : "Johhnyte",
#     "last_name" : "Napoles",
#     "age" : 32,
#     "average" : 81.76, 
#     "list_subjects" : ["Programming", "Mathematics", "English"]
# },
# {
#     "first_name" : "Rose",
#     "last_name" : "Tadea",
#     "age" : 32,
#     "average" : 82.54, 
#     "list_subjects" : ["Programming", "Mathematics", "English"]
# },
# {
#     "first_name" : "Angel",
#     "last_name" : "Tadea",
#     "age" : 32,
#     "average" : 86, 
#     "list_subjects" : ["Programming", "Mathematics", "English"]
# },
# ]

# for key in list_of_users:
#     for x in key:
#         print(x, key[x])

# looping in reversed
x = range(1,10)
for i in x[::-1]:
    print(i)