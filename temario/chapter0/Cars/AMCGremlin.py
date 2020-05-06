#!/usr/bin/env python
# -*- coding: utf-8 -*-


class AMCGremlin:
	def __init__(self): 
		self.models = ['q7', 'a6', 'a8', 'a3'] 

	def __del__(self):
		print("Se ha destruido el objeto AMCGremlin")

	def outModels(self):
		print('Following models of AMC Gremlin is available now:')
		for model in self.models:
			print(model)