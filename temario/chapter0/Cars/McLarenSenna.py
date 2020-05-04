#!/usr/bin/env python
# -*- coding: utf-8 -*-


class McLarenSenna: 
    def __init__(self):
        self.models = ['altima', '370z', 'cube', 'rogue'] 

    def outModels(self): 
        print("Following models of McLaren Senna is available with us now:") 
        for model in self.models: 
            print(model)