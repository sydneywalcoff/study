# for loops
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

# for game in board_games:
#   print(game)

# for sport in sport_games:
#   print(sport)

# for loops: ranges
promise = "I will finish the python loops module!"

# for i in range(5):
#     print(promise)

countdown = 10
# while countdown >= 0:
#   print(countdown)
#   countdown -= 1

# print("We have liftoff!")

# list
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0

# while index < length:
#     print("I am learning about " + python_topics[index])
#     index+= 1


# loop control: break
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

# for dog_breed in dog_breeds_available_for_adoption:
#     print(dog_breed)
#     if dog_breed == dog_breed_I_want:
#         break
# print("They have the dog I want!")


# loop control: continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

# for age in ages:
#     if age < 21:
#         continue
#     print(age)


# nested loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for store in sales_data:
    for scoop in store:
        scoops_sold += scoop

# print(scoops_sold)


# list comprehensions
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [score + 10 for score in grades]
# print(scaled_grades)

# list comprehensions: conditionals
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)


# review
single_digits = range(0,10)
squares = []

for digit in single_digits:
  print(digit)
  squares.append(digit**2)

print(squares)

cubes = [ digit**3 for digit in single_digits]
print(cubes)