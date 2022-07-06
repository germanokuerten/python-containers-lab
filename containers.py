################################
## Python Containers - Lab
################################

## Exercise 1

# Create a list named studentscontaining some student names (strings).

from re import A


students = [
    'Germano Kuerten',
    'Alejandro Rojas',
    'Cheryl Weigel',
    'Brianna Gaines',
    'Joan Renfroe'
]

# Print out the second student's name.

print(students[1])

# Print out the last student's name.

print(students[-1])

################################

## Exercise 2

# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.

foods = (
    'Açaí Bowl',
    'Banana Smoothie', 
    'Dark Chocolate',
    'Super Foods',
    'Rice and Beans'
)

#Use a for loop to print out the string "food goes here is a good food".

for food in foods:
    print(f'{food} is a good food!')

################################

## Exercise 3

# Using a for loop, print just the last two food strings from foods.

for food, var in enumerate(foods):
    if food == len(foods) - 2:
        print (var)
    if food == len(foods) - 1:
        print(var)

################################

## Exercise 4

# Create a dictionary named home_town containing the keys of city, state and population.

home_town = {
    'city': 'Laguna',
    'state': 'Santa Catarina',
    'population': 46122
}

# Print a string with this format: 
# "I was born in city, state - population of population"

print(f'I was born in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}')

################################

## Exercise 5

# Iterate over the key: value pairs in home_town and print a string for each item, for example:

for key, value in home_town.items():
    print(f'"{key} = {value}"')


################################

## Exercise 6

# Create an empty list named cohort.

cohort = []

# Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape: 

# I am not sure what is being asked here, so I will just assume the following.


for student, food in zip(students, foods):
    cohort.append({
        "student": student,
        "fav_food": food
    })

print(cohort)

# {
# 	'student': 'Tina',
# 	'fav_food': 'Cheeseburger'
# }

# Iterate over cohort printing out each element.

################################

## Exercise 7

# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]

awesome_students = [n + ' is awesome!' for n in students]
print(awesome_students)

# Iterate over awesome_studentsprinting out each string.

################################

## Exercise 8

# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.

print('done')

foods_with_letter_a = [n for n in foods if 'a' in n or 'A' in n]
print(foods_with_letter_a)