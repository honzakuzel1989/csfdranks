#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sort_movies(sort, items, key):
	if sort:
		items.sort(key=lambda p: p[key])

