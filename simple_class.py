# Derek Baker 10353830

# This code will look at the changes_python.log and evaluate:
# 1 Time of report
# 2 Number of lines in the file
# 3 Number of commits in the file
# 4 Number of Authors in file
# 5 Frequency of commits by author
# 6 Top 5 authors
# 7 The author with the highest commits (just to show different code than above line)
# 8 Top 5 dates with most commits
# 9 First commit Date
# 10 Last commit Date
# 11 Length of time between first and last commit
# 12 Length of time since last commit
# 13 Last commit revision number
# 14 Runtime of report


# Used to do date ranges and current time
import datetime

# Set current datetime
report_start_time = datetime.datetime.now()

# Use to clear the screen for each run of code
import os 
os.system('cls')


##### Input #####
# open the file - and read all of the lines.
changes_file = 'changes_python.log'
def read_file():	
# use strip to strip out spaces and trim the line.
	data = [line.strip() for line in open(changes_file, 'r')]
	return data

data = read_file()

##### Analyse #####
sep = 72*'-'

# create the commit class to hold each of the elements
class Commit:
#Initialise
	def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
		self.revision = revision
		self.author = author
		self.date = date
		self.comment_line_count = comment_line_count
		self.changes = changes
		self.comment = comment
# Get comments - not used 
#	def get_commit_comment(self):
#		return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
#				+ self.author + ' with the comment ' + ','.join(self.comment) \
#				+ ' and the changes ' + ','.join(self.changes)

# Churn the data
def parse_data(data):
# Create lists and set index to zero
	commits = []
	current_commit = None
	index = 0
	revisions = []
	authors = []
	dates = []
# Loop the data
	while True:
		# Use Failsafe
		try:
			# parse each of the commits and put them into a list of commits
			current_commit = Commit()
			details = data[index + 1].split('|')
			current_commit.revision = int(details[0].strip().strip('r'))
			current_commit.author = details[1].strip()
			current_commit.date = details[2].strip()
			current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
			current_commit.changes = data[index+2:data.index('',index+1)]
			#print(current_commit.changes)
			index = data.index(sep, index + 1)
# Not Used -current_commit.comment = data[index-current_commit.comment_line_count:index]
			commits.append(current_commit)
			authors.append(current_commit.author)
			revisions.append(current_commit.revision)
			# Split the date to remove time
			dates_split = current_commit.date.split(' ')
			date_part = dates_split[0]
			dates.append(date_part)
		except IndexError:
			break
	return (commits, authors, dates, revisions)

commits, authors, dates, revisions = parse_data(data)

# Put authors into a dict
def get_authors(commits, authors):
	authors_dict = {}
	for author in authors:
		if author in authors_dict:
			authors_dict[author] = authors_dict[author] + 1
		else:
			authors_dict[author] = 1
	return authors_dict

authors_dict = get_authors(commits, authors)

##### Output #####
print '-' * 31 # These are used for display purposes only

# Show datetime report created
startime = str(report_start_time).split('.')
print 'Time of report: ', startime[0]
print '-' * 31

# Output the number of lines read
num_lines = (len(data))
print 'Number of lines in the file: ', num_lines 

# Output the number of commits
num_commits = (len(commits))
print 'Number of commits in the file: ', num_commits

# Output the number of authors
num_authors = (len(authors_dict))
print 'Number of Authors in file: ', num_authors
print '\n'

##### Authors #####
print '#'*10, ' Authors ', '#'*10 # For display only
print '-' * 31

# analyse the authors for frequency
def get_authors_frequency():
	for key, value in sorted(authors_dict.items()):
		print value,'	',round(float(value)/len(authors)*100,2),'	',key

#Output author_frequency
print 'Count','	','Percent','	','Author' # Header of output
print '-' * 31
get_authors_frequency() # This can't be tested in current format as no variable has been created

print '\n' # for display only
print '-' * 31

# Find the Top 5 authors
import collections 
def top_5_authors():
	author_counter = collections.Counter(authors_dict)
	for count in author_counter.most_common(5):
		print  (str(count[1]) + '	' + str(count[0]))

# Output top 5 authors
print 'Top 5 authors' # Title of top 5 authors
print '-' * 31
top_5_authors() # # This can't be tested in current format as no variable has been created

print '\n'
print '-' * 31

# Find author with most revisions added
def top_author():
	all_authors_items = authors_dict
	max_Author = [0]
	while all_authors_items:
		key, value = all_authors_items.popitem()
		if value > max_Author[0]:
			max_Author = [value,[key]]
		elif value == max_Author[0]:
			max_Author[1].append(key)
	print 'The author with the highest commits: ',max_Author

# Output author with highest commits
top_A = top_author()

print '-' * 31
print '\n'

########## DATES ##############
print '#'*10, ' Dates ', '#'*10 # Display only
print '-' * 31

# Create a dates dict and analyse dates
dates_dict = {}
for date in dates:
	if date in dates_dict:
		dates_dict[date] = dates_dict[date] + 1
	else:
		dates_dict[date] = 1

# Find the Top 5 popular dates

print 'Top 5 dates with commits' # For Title
print '-' * 31
print 'Count','	','Date' # Header of Top 5 dates

# Find the Top 5 dates with commits
def top_5_dates():
	date_counter = collections.Counter(dates_dict)
	amc = counter.most_common()[0]
	for count in date_counter.most_common(5):
		print  (str(count[1]) + '	' + str(count[0]))
	print '\n'
	print '-' * 31
	print amc[0],'	','Mode of commits\n' ,amc[1],'	','Instances of mode'
# Output the Top 5 dates with commits		
top_5_dates() # This can't be tested in current format as no variable has been created

#get all the keys from dates_dict and store them to a list
allKeys = dates_dict.keys()
#sort the list of keys
allKeysSorted = sorted(allKeys)
#retrieve the first and last keys in the list
firstKey = allKeysSorted[0]
lastKey = allKeysSorted[-1]

print '\n'
print '-' * 31

# Find and output first and last commit date
f_c_d = str(firstKey)
print 'First commit Date: ', f_c_d 
l_c_d = str(lastKey) 
print 'Last commit Date: ', l_c_d

print '-' * 31

# Find start and end date of project that can be used to calculate range
start_date_range = datetime.datetime(2015,07,13)#  couldn't work out how to get the date in here automatically
last_date_range = datetime.datetime(2015,11,27)# no point in testing as the value is hard coded
# Calculate date range of project
date_range = str(last_date_range - start_date_range).split(',')
# Output date range of project
print 'Length of time between first and last commit: ', date_range[0]

# Find lenght of time since end of project
to_date_range = str(report_start_time - last_date_range).split(',')
# Output lenght of time since end of project
print 'Length of time since last commit: ', to_date_range[0]

print '-' * 31

# Find and output last revision number
last_revision_number = sorted(revisions)[-1]
print 'Last commit revision number: ', last_revision_number

print '-' * 31

# Find and output runtime of report
report_end_time = datetime.datetime.now()
run_time = report_end_time - report_start_time

#Output report runtime
print 'Runtime of report: ', run_time #Can't test as output varies
print '-' * 31
