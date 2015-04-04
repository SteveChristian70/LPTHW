# importing argument
from sys import argv

script, filename = argv

# setting open(filename) to txt
txt = open(filename)

# printing the file name
print "Here's your file %r:" % filename 

# opening the file and printing it
print txt.read()
txt.close()

# asking for you to type the file name to read the file
print "Type the filename again:"

file_again = raw_input("> ")

# setting txt to open file again 
txt_again = open(file_again)

# reading and printing txt again
print txt_again.read()

txt_again.close()