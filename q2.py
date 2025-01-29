# Make a random pet.
import random
# Choose:
# Type of animal (at least 3 choices, string)
animal = random.choice(["dog", "cat", "fish", "kyle"])
# Age (integer)
age = random.randint(1,30)
# Color (at least 3 choices, string)
color = random.choice(["orange", "purple", "green"])
# Weight (float)
if animal == "kyle":
    weight = random.uniform(10000,20000)
else:
    weight = random.uniform(1,75)

# Print a summary of your pet using an f-string
print(f"Your pet is a {animal}, that is {age} years old, is {color}, and weighs {weight} lbs")