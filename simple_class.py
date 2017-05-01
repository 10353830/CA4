# Derek Baker 10353830

# Used to do date ranges and current time
import datetime
# Set current datetime
report_start_time = datetime.datetime.now()
# Use to clear the screen for each run of code
import os 
os.system('cls')
### Input ###

def read_file(changes_file):

	# use strip to strip out spaces and trim the line.

	data = [line.strip() for line in open(changes_file, 'r')]

	return data

## open the file - and read all of the lines.
changes_file = 'changes_python.log'
## use strip to strip out spaces and trim the line.
data = [line.strip() for line in open(changes_file, 'r')]

### Analyse ###
sep = 72*'-'

# create the commit class to hold each of the elements

class Commit:

	def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
		self.revision = revision
		self.author = author
		self.date = date
		self.comment_line_count = comment_line_count
		self.changes = changes
		self.comment = comment

	def get_commit_comment(self):
		return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
				+ self.author + ' with the comment ' + ','.join(self.comment) \
				+ ' and the changes ' + ','.join(self.changes)
   

commits = []
current_commit = None
index = 0
revisions = []
authors = []
dates = []
while True:
	try:
		# parse each of the commits and put them 	to a list of commits
		current_commit = Commit()
		details = data[index + 1].split('|')
		current_commit.revision = int(details[0].strip().strip('r'))
		current_commit.author = details[1].strip()
		current_commit.date = details[2].strip()
		current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
		current_commit.changes = data[index+2:data.index('',index+1)]
#print(current_commit.changes)
		index = data.index(sep, index + 1)
		current_commit.comment = data[index-current_commit.comment_line_count:index]
		commits.append(current_commit)
		authors.append(current_commit.author)
		revisions.append(current_commit.revision)
# Split the date to remove time
		dates_split = current_commit.date.split(' ')
		date_part = dates_split[0]
		dates.append(date_part)
	except IndexError:
		break

### Output ###
print '-' * 31

# Show datetime report created
print 'Time of report: ', report_start_time
print '-' * 31
# print the number of lines read
print 'Number of lines in the file: ', (len(data))
# print the number of commits
print 'Number of commits in the file: ',(len(commits))
print '\n'

##### Authors #####
print '#'*10, ' Authors ', '#'*10
print '-' * 31

def get_authors(commits):
	authors_dict = {}
	for author in authors:
		if author in authors_dict:
			authors_dict[author] = authors_dict[author] + 1
		else:
			authors_dict[author] = 1
	return authors_dict

authors_dict = get_authors(commits)

# Put the authors into a dict and analyse the authors for frequency
#authors_dict = {}
#for author in authors:
#	if author in authors_dict:
#		authors_dict[author] = authors_dict[author] + 1
#	else:
#		authors_dict[author] = 1
print 'Count','	','Percent','	','Author'
print '-' * 31
for key, value in sorted(authors_dict.items()):
	print  value,'	',round(float(value)/len(authors)*100,2),'	',key
print '\n'
print '-' * 31
# Get the Top 5 authors
# Use to find top 5 dates
import collections 
print 'Top 5 authors'
print '-' * 31
author_counter = collections.Counter(authors_dict)
for count in author_counter.most_common(5):
	print  (str(count[1]) + '	' + str(count[0]))
	
print '\n'
print '-' * 31

# Find author with most revisions added
all_authors_items = authors_dict
max_Author = [0]
while all_authors_items:
	key, value = all_authors_items.popitem()
	if value > max_Author[0]:
		max_Author = [value,[key]]
	elif value == max_Author[0]:
		max_Author[1].append(key)
print 'The author with the highest commits: ',max_Author

print '-' * 31
print '\n'

########## DATES ##############
print '#'*10, ' Dates ', '#'*10
print '-' * 31



# Create a dates dict and analyse dates
dates_dict = {}
for date in dates:
	if date in dates_dict:
		dates_dict[date] = dates_dict[date] + 1
	else:
		dates_dict[date] = 1

# get the Top 5 most popular dates
date_counter = collections.Counter(dates_dict)
print 'Top 5 dates with most commits' 
print '-' * 31
print 'Count','	','Date'
for count in date_counter.most_common(5):
	print  (str(count[1]) + '	' + str(count[0]))


#get all the keys and store them to a list
allKeys = dates_dict.keys()

#sort the list of keys
allKeysSorted = sorted(allKeys)

#retrieve the first and last keys in the list
firstKey = allKeysSorted[0]
lastKey = allKeysSorted[-1]
print '\n'
print '-' * 31
# Output first and last commit date
print 'First commit Date: ' + str(firstKey)
print 'Last commit Date: ' + str(lastKey) 


print '-' * 31
# Get 
start_date_range = datetime.datetime(2015,07,13)#  couldn't work out how to get the date in here automatically
last_date_range = datetime.datetime(2015,11,27)
print 'Length of time between first and last commit: ',  last_date_range - start_date_range
print 'Length of time since last commit: ', report_start_time - last_date_range 

#print 'test2'
#start_date_range = str(firstKey)#  couldn't work out how to get the date in here automatically
#last_date_range = str(lastKey)
#print 'Length of time between first and last commit: ',  last_date_range - start_date_range
#print 'Length of time since last commit: ', now - last_date_range 
print '-' * 31

print 'Last commit revision number: ',sorted(revisions)[-1]
print '-' * 31
# Show runtime of report
report_end_time = datetime.datetime.now()
print 'Runtime of report: ', report_end_time - report_start_time
print '-' * 31