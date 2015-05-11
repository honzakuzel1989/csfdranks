#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

def parse_arguments():
	parser = ArgumentParser()

	parser.add_argument("source", type=str, help="the data source")
	parser.add_argument("--source_type", type=str, choices=["html"], default="html", help="the data source type")
	parser.add_argument("-s", "--sort_by", type=str, choices=["order", "film", "average", "count", "rating"], default=None, help="the key for sorting output")
	parser.add_argument("-o", "--output_type", type=str, choices=["simple", "stats"], default=None, help="the type of the output")

	args = parser.parse_args()
	return args	

