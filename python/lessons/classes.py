# Types
# print(type(5)) # int
my_dict = {}
# print(type(my_dict)) # dict
my_list = []
# print(type(my_list)) # list

# instantiation
class Facade:
  pass # pass tells compiler that we want empty class

facade_1 = Facade() # instantiation

facade_1_type = type(facade_1)
# print(facade_1_type) # <class '__main__.Facade'>

# class variables
class Grade:
  minimum_passing = 65

# methods
class Rules:
  def washing_brushes(self):
      return "Point bristles towards the basin while washing your brushes."

# methods with arguments
class Circle:
  pi = 3.14
  
  def area(self, radius):
      return self.pi * radius ** 2

circle = Circle()
pizza_area = circle.area((12/2))
teaching_table_area = circle.area((36/2))
round_room_area = circle.area((11460/2))

# constructors
# dunder methods - double underscore on either side. ex) __init__()

class Circle1:
  pi = 3.14
  def __init__(self, diameter):
    # print("New circle with diameter: "+ str(diameter))
    pass # added to be able to comment out print statement

# teaching_table = Circle(36) # prints New circle with diameter: 36

# instance variables
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = 'Alternative Rocks'
isabelles_ices.store_name = "Isabelle's Ices"


# attribute functions
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
for element in can_we_count_it:
  if hasattr(element, "count"):
    # print(str(type(element)) + " has the count attribute!") # lists and dictionaries
    pass
  else:
    # print(str(type(element)) + " does not have the count attribute :(") # str ints floats
    pass

# self
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    # print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter/2
  def circumference(self):
    return 2 * self.pi * self.radius


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

# print(medium_pizza.circumference()) # 37.68
# print(teaching_table.circumference()) # 113.04
# print(round_room.circumference()) # 35984.4


# Directories

# print(dir(5)) 

def this_function_is_an_object():
  return ':)'

# print(dir(this_function_is_an_object)) 

# String representation

class Circle2:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  def __repr__(self):
    return 'Circle with radius ' + str(self.radius)
  
medium_pizza2 = Circle2(12)
teaching_table2 = Circle2(36)
round_room2 = Circle2(11460)

print(medium_pizza2)
print(teaching_table2)
print(round_room2)