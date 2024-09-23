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

for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        break
print("They have the dog I want!")