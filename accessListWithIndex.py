animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]

# The fourth through sixth characters
dog = animals[3:6]

# From the seventh character to the end
frog = animals[6:len(animals)]

print cat
print dog
print frog


#Maintaining order
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")

# Your code here!
animals.insert(duck_index, "cobra")

print animals # Observe what prints after the insert operation