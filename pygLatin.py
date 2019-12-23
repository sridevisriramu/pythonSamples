word = raw_input("enter a word in english : ")
if(len(word) >0):
 print "user entered valid word"
length=int(len(word))
#print str(word[length-len(word)] +word[2]+word[3]+word[0])+"ay"

subString=word[1:length]
print word[0]
print subString +word[0] +"ay"