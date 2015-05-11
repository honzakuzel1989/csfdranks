#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('modules')

from csfdranks_printer import print_movies
from csfdranks_sorter import sort_movies
from csfdranks_args_parser import parse_arguments
from csfdranks_src_parser import parse_source

def main():
	args = parse_arguments()
	movies = parse_source(args.source, args.source_type)
	sort_movies(args.sort_by, movies, args.sort_by)
	print_movies(movies, args)

if __name__ == '__main__':
	main()

