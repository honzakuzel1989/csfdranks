#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup

def parse_source(source, source_type):
	data = None
	if source_type == "html":
		data = __parse_html_source(source)
	
	return data

def __parse_html_source(source):
	soup = None
	with open(source, "r") as ifile:
		html = ifile.read()
		soup = BeautifulSoup(html)
	
	movies = []

	content = soup.find('div', id='results')
	table = content.find('table')
	rows = table.findAll('tr')
	for r in rows:
		cols = r.findAll('td')
		order, film, average, count, rating, link = None, None, None, None, None, None
		for c in cols:
			cls = c['class']
			text = c.find(text=True)
			if "order" == cls:
				order = int(text[:-1])
			elif "film" == cls:
				a = c.find('a')
				film = text
				link = a['href']
				# convert relative url to absolute url
				if not "http://www.csfd.cz" in link:
					link = "http://www.csfd.cz" + link
			# the class is "average" in best movies abut "average info" in favoritmovies
			elif "average" == cls or "average info" == cls:
				average = text
			elif "count" == cls: 
				count = text
			elif "rating" == cls:
				img = c.find('img')
				if img:
					rating = len(img['alt'])
				else:
					rating = 0

		movies.append({'order':order, 'film':film, 'average':average, 'count':count, 'rating':rating, 'link':link})
	
	return movies

import unittest

class CsfdRanksSrcParserTest(unittest.TestCase):
	def test_parse_html_source(self):
		# input test file
		first = None
		with open("csfdranks_src_parser.test.1", "r") as oneFile:
			first = oneFile.read()
		# parsered output for known input
		second = parse_source("csfdranks_src_parser.test.in", "html")

		# remove empty items from list
		one = filter(bool, first.split('\n'))
		# convert all items to string
		two = map(str, second)
		# compare two lists of strings
		self.assertTrue(one == two)

if __name__ == '__main__':
	unittest.main()

