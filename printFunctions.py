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