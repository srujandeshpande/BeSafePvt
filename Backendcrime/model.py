# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 00:32:35 2019

@author: Tanvy
"""

import pandas as pd
import numpy as np
import gmplot

import matplotlib.pyplot as plt

import folium
from IPython.display import display

import sklearn
import sklearn.preprocessing as preprocessing
import sklearn.model_selection as mdl
import sklearn.cluster as cluster

#import sklearn.model_selection as mdl
import sklearn.metrics as mat
import sklearn.svm as svm


import random

class Model():
    classifier = ''
    def startModel(self):
        accident2 = pd.read_csv('crime2019.csv')
        accident = accident2[['LocType','Time','offence','Latitude','Longitude']]

        #accident["DATE"] = pd.to_datetime(accident["DATE"])
        #accident.index = accident["DATE"]
        
        accident = accident.replace(' ', np.NAN, regex=False)
        
        
        accident["LocType"][accident["LocType"].isnull()]
#        print(len(accident["District"][accident["District"].isnull()]))
        accident["LocType"][accident["LocType"].isnull()] = "RESTAURANTS"
#        print(len(accident["District"][accident["District"].isnull()]))
        
        accident["Time"][accident["Time"].isnull()]
#        print(len(accident["ROAD_CLASS"][accident["ROAD_CLASS"].isnull()]))
        #accident["ROAD_CLASS"][accident["ROAD_CLASS"].isnull()] = "Major Arterial"
#        print(len(accident["ROAD_CLASS"][accident["ROAD_CLASS"].isnull()]))


        accident["offence"][accident["offence"].isnull()]
#        print(len(accident["STREET2"][accident["STREET2"].isnull()]))
        accident["offence"][accident["offence"].isnull()] = "THEFT"
#        print(len(accident["STREET2"][accident["STREET2"].isnull()]))


       

        enc = preprocessing.LabelEncoder()
        enc.fit(accident["LocType"])
        new_cat_features = enc.transform(accident["LocType"])
#        print(new_cat_features) # [1 2 0]
        accident["LocType"] = new_cat_features

        enc = preprocessing.LabelEncoder()
        enc.fit(accident["Time"])
        new_cat_features = enc.transform(accident["Time"])
#        print(new_cat_features) # [1 2 0]
        accident["Time"] = new_cat_features        
 
        enc = preprocessing.LabelEncoder()
        enc.fit(accident["offence"])
        new_cat_features = enc.transform(accident["offence"])
#        print(new_cat_features) # [1 2 0]
        accident["offence"] = new_cat_features

       
        
        accidentValue = accident.iloc[:,:]
        accidentValue = accidentValue.reset_index()
        #accidentValue = accidentValue.drop(axis=1)
        
        accidentValue = accidentValue.values
        
        kmeans = cluster.KMeans(n_clusters=2, init="k-means++", max_iter=300, n_init=10, random_state=0)
        yMeans = kmeans.fit_predict(accidentValue)
        self.yMeans = yMeans
        self.classifier = svm.SVC(kernel='linear', random_state=0)
        self.classifier.fit(accidentValue, yMeans)
    
    def Predict(self, par):
        return self.classifier.predict(par)
       
def Main():
    pass