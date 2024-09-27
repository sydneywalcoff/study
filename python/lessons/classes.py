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