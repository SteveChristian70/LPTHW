from sys import argv
# script from exercise16.py filename from test.txt
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# waits for command
raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
# erases the file contents
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to write these to the file."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

# condenced version of write
target.write("%s\n%s\n%s\n" % (line1, line2, line3))


print "And finally, we close it."
target.close()