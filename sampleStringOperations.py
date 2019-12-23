float_1 = 0.25
float_2 = 40.0

age = 13
print "I am " + str(age) + " years old!"

number1 = "100"
number2 = "10"

string_addition = number1 + number2 
print string_addition
#string_addition now has a value of "10010"

int_addition = int(number1) + int(number2)
print int_addition
#int_addition has a value of 110

string1 = 3.5
print(int(string1))
print(float(string1))

product=(float(float_1))*float_2
print(product)

big_string="The product was " + str(product)
print big_string


skill_completed ="Python Syntax"
exercises_completed=13
#The amount of points for each exercise may change, because points don't exist yet
points_per_exercise=5
point_total=100
point_total+=(exercises_completed*points_per_exercise)

print "I got " +str(point_total)+" points!"
