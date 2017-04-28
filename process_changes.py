# Open the changes file and read all the lines
changes_file = 'changes_python.log'
# look at the file
the_file = open(changes_file, 'r')
#print the_file

# Look at the data inside the file
data = the_file.readlines()

#Output the data
#print data

#Find the count of lines in the file
print "There are {} lines in the file".format(len(data))

#Find the count of revisions no Class
sep = 72*'-'
revision_count = 0
for line in data:
	if sep in line:
		revision_count+=1
		continue
print "There are {} revisions in the file".format(revision_count -1)

