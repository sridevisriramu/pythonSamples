"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "MONTY"[4]

print fifth_letter

ministry = "The Ministry of Silly Walks"

print len(ministry)
print str(ministry)
print ministry.upper()

string_1 = "Camelot"
string_2 = "place"
Str3="test3"

print "Let's not go to %s. 'Tis a silly %s. this is test for %s." % (string_1, string_2, Str3)
                                                
name = "Mike"
print "Hello %s" % (name)

day =7

print "03 - %s - 2019" % (day)
print "03 - %03d - 2019" % (day)


name = raw_input("What is your name? ")
quest = raw_input("What is your quest? ")
color = raw_input("What is your favorite color? ")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)