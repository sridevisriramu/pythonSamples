def using_control_once():
    if (3>2):
        return "Success #1"

def using_control_again():
    if  True:
        return "Success #2"

print using_control_once()
print using_control_again()

answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return  False      # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False  # Make sure this returns False
      
print black_knight()
print french_soldier()

def greater_less_equal_5(answer):
    if answer>5:
        return 1
    elif answer<5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)


# Complete the if and elif statements!
def grade_converter(grade):
    if grade>=90:
        return "A"
    elif grade<=80 and grade >75:
        return "B"
    elif grade>=68 and grade==70:
        return "C"
    elif grade >64 and grade <68:
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print grade_converter(92)

# This should print a "C"
print grade_converter(70)

# This should print an "F"
print grade_converter(61)