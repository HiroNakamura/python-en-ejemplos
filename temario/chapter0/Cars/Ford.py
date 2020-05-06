#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Ford:
	def __init__(self):
		self.models = ['i8', 'x1', 'x5', 'x6']

	def __del__(self):
		print("Se ha destruido el objeto Ford")

	def outModels(self):
		print('Following models of Ford is available now:')
		for model in self.models:
			print(model)