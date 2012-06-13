#!/usr/bin/python

#join to String , split to array
strs = ['Hello' , 'World' , 'Alan.P']
result = "|".join(strs)
#print result

str = "abcdefg";

# start 2 to 5
print str[2:5]

#step 2
print str[::2]

sentence  = 'Non dsif:1,2,3,4'

print sentence.split(',')

print sentence.split(',',2)

#find (if no return -1)
print sentence.find('sif')

#replace String
print sentence.replace('if', 'Alan')