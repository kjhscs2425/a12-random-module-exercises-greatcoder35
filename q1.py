import random
def spin_twister_spinner():
  """
  Returns a list with a random color, side, and appendage
  
  colors: "red", "green", "yellow", or "blue"
  sides: "left" or "right"
  appendage: "hand" or "foot"
  """
  #YOUR CODE HERE
  colors = random.choice(["red", "green", "yellow", "blue"])
  sides = random.choice(["left", "right"])
  appendage = random.choice(["hand", "foot"])
  return print(f"Place your {sides} {appendage} on {colors}")

# Here's the function call. This should print a random assortment of twister commands
for _ in range(10):
  spin_twister_spinner()