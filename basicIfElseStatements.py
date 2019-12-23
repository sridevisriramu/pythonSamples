def testIfElseFlow():
  print "test if else flows"
  result=raw_input("enter favorite color ? ").lower()
  if(result=="red" or result=="r"):
     print "you like red color"
	 
  elif (result=="pink" or result=="p"):
      print "you like pink color"
	  
  else:
      print "you like other color than pink and red"

testIfElseFlow()