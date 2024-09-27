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
    print("New circle with diameter: "+ str(diameter))

# teaching_table = Circle(36) # prints New circle with diameter: 36
    