# Derek Baker 10353830

# This test file will test simple_class.py 
# The tests included are:
# 1 Validate the correct file is used
# 2 Test the number of lines
# 3 Test the number of commits
# 4 Test the number of authors
# 5 Test the first and last authors to commit
# 6 Test the first and last revision numbers
# 7 Test top author
# 8 Test first and last dates_dict keys
# 9 Test first and last dates_dict keys after sorting 
# 10 Test first key as string
# 11 Test last key as string
# 12 Test project date range
# 13 Test first element of dates_dict
# 14 Test runtime is greater than zero

import unittest

from simple_class import * # read_file,get_authors_frequency

class TestCommits(unittest.TestCase):

	def setUp(self):
		self.data = read_file()
		
	def test_changes_file(self):
		self.assertEqual('changes_python.log',changes_file)

	def test_num_lines(self):
		self.assertEqual(5255, num_lines)

	def test_num_commits(self):
		commits = parse_data(self.data)[0]
		self.assertEqual(422, num_commits)
		
	def test_num_authors(self):
		commits, authors, dates, revisions = parse_data(self.data)
		authors = get_authors(commits, authors)
		self.assertEqual(10, num_authors)

	def test_first_last_commit(self):
		commits, authors, dates, revisions = parse_data(self.data)
		self.assertEqual('Thomas', commits[0].author)
		self.assertEqual('Thomas', commits[-1].author)
		
	def test_first_last_revision(self):
		commits, authors, dates, revisions = parse_data(self.data)
		self.assertEqual(1551925, commits[0].revision)
		self.assertEqual(1491146, commits[-1].revision)
		
	def test_top_author(self):
		commits, authors, dates, revisions = parse_data(self.data)
		authors = get_authors(commits, authors)
		self.assertEqual(191, authors['Thomas'])
		
	def test_allKeys(self):
		self.assertEqual('2015-10-16',allKeys[0])
		self.assertEqual('2015-09-22',allKeys[-1])
		
	def test_allKeysSorted(self):
		self.assertEqual('2015-07-13',allKeysSorted[0])
		self.assertEqual('2015-11-27',allKeysSorted[-1])

	def test_first_commit_date(self):
		self.assertEqual('2015-07-13', f_c_d)

	def test_last_commit_date(self):
		self.assertEqual('2015-11-27', l_c_d)
		
	def test_date_range(self):
		self.assertEqual('137 days',date_range[0])
		
	def test_dates_dict(self):
		self.assertEqual('2015-10-16',dates_dict.keys()[0])
		
	def test_start_end(self):
		self.assertEqual(report_start_time < report_end_time, True)

if __name__ == '__main__':
	unittest.main()
