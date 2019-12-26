"""
Changing Your Mind
Because dictionaries are mutable, they can be changed in many ways. Items can be removed from a dictionary with the del command:

del dict_name[key_name]
will remove the key key_name and its associated value from the dictionary.

A new value can be associated with a key by assigning a value to the key, like so:

dict_name[key] = new_value
"""

# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

zoo_animals['Rockhopper Penguin']= 'test new value'

# Your code here!




print zoo_animals