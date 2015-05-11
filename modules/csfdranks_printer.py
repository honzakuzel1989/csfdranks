#!/usr/bin/env python
# -*- coding: utf-8 -*-

def print_movies(movies, args):
	if args.output_type == "simple":
		__print_simple(movies)
	elif not args.output_type:
		__print_table(movies)
	elif args.output_type == "stats":
		__print_statistics(movies)

def __print_simple(items):
		for i in items:
			print u"{}. {} ({}) - {} {} [{}]".format(i['order'], i['film'], i['link'], i['average'], "("+i['count']+")", i['rating']).encode('utf-8')

def __print_table(items):
	for i in items:
		print u"{:<3} {:<50}{:<75}{:<6}{:<25}{}".format(str(i['order']) + ".", i['film'], i['link'], i['average'], "("+i['count']+")", i['rating']).encode('utf-8')

def __print_statistics(items):
	count = len(items)
	seen = 0
	unseen = 0
	for m in items:
		if m['rating']:
			seen += 1
		else:
			unseen += 1
	print u"count:{} seen:{} unseen:{}".format(count, seen, unseen)
		
