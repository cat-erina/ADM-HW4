#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 21:42:44 2019

@author: ujafarli
"""

"""
Since Clustering algorithms are for unsupervised data,chance of getting less optimal result is 
possible.One reason is differently from supervised learning, here we define k(number of clusters) 
as an input,it is not learned from data.In Random Initialization,the initial centroids is randomly
chosen by k-means,which is randomly assigned to some points.In another kind of initialization, 
Forgy Method, the initial points chosen by dataset. Generally, Forgy method is more successful
than Random Initialization. There is also k-means++ which is improved version for handling poor 
clustering. Considering properties of clustering such as number of clusters, cluster overlap, 
balance or unbalance, inilialization is important to get optimal result. In a poor cluster cost 
function(error between actual and predicted value) is high while in good cluster cost function is 
less(because of less error). 
"""