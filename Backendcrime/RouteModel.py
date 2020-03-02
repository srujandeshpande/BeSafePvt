# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 00:11:46 2019

@author: Tanvy
"""
import model

class RouteSafer:
    def __init__(self, LocType, Time,offence):
        self.LocType = LocType
        self.Time  = Time
        self.offence   = offence
       
        
        md = model.Model()
        md.startModel()
        d = [self.LocType, self.Time, self.offence]
             
        print(md.Predict([d]))

if __name__ == '__main__':
    rs = RouteSafer(1, 1, 1)
    