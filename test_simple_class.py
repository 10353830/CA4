
import unittest

from simple_class import * # read_file,get_authors_frequency

class TestCommits(unittest.TestCase):

	def setUp(self):
		self.data = read_file('changes_python.log')

	def test_number_of_lines(self):
		self.assertEqual(5255, len(self.data))

	def test_number_of_commits(self):
		commits = parse_data(self.data)[0]
		self.assertEqual(422, len(commits))
		
	def test_number_of_authors(self):
		commits, authors, dates, revisions = parse_data(self.data)
		authors = get_authors(commits, authors)
		self.assertEqual(10, len(authors))

	def test_first_commit(self):
		commits, authors, dates, revisions = parse_data(self.data)
		self.assertEqual('dave.ramsey', commits[0].author)
		self.assertEqual(1551925, commits[0].revision)
		
	def get_authors_freq(self):
		self.assertEqual(12,get_authors_frequency())
	
	def test_top_author(self):
		commits, authors, dates, revisions = parse_data(self.data)
		authors = get_authors(commits, authors)
		self.assertEqual(191, authors['dave.ramsey'])



if __name__ == '__main__':
	unittest.main()
