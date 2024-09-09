my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')

my_single_tuple = ('abc',)

# indexing and slicing

print(my_tuple[0]) # prints abc

print(my_tuple[3:5]) # prints (456, 789)

# len()
print(len(my_tuple)) # prints 6

# max()
my_tuple = (65, 2, 88, 101, 25)
max(my_tuple) # returns 101
my_tuple = ('orange', 'blue', 'red', 'green')
max(my_tuple) # returns "red"
my_tuple = ('abc', 234, 567, 'def')
max(my_tuple) # throws an error!

# min()
my_tuple = (65, 2, 88, 101, 25)
min(my_tuple) # returns 2
my_tuple = ('orange', 'blue', 'red', 'green')
min(my_tuple) # returns "blue"
my_tuple = ('abc', 234, 567, 'def')
min(my_tuple) # throws an error!

# .index()
my_tuple = ('abc', 234, 567, 'def')
my_tuple.index('abc') # returns 0
my_tuple.index(567) # returns 2

# .count()
my_tuple = ('abc', 'abc', 2, 3, 4)
my_tuple.count('abc') # returns 2
my_tuple.count(3) # returns 1
