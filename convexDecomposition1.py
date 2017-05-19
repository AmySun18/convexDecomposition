# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 16:00:27 2016

@author: xmsun
"""

import py2d
import py2d.Math as pm
import pylab as plt
import numpy as np
#%%
#t = [(1,1),(1,2),(2,2),(2,1),(1,1)]
t = [(1,1),(1,2),(2,2),(2,1)]
#t = [(1,1),(1,20),(20,20),(20,1),(1,1)]
missionSpace =py2d.Math.Polygon.from_tuples(t)
#Polygon [(1.00, 1.00), (1.00, 2.00), (2.00, 2.00), (2.00, 1.00), (1.00, 1.00)]
#hole = [(1.2, 1.2),(1.5,1.2),(1.5 ,1.5),(1.2,1.5) ,(1.2,1.2)]
hole = [(1.2, 1.2),(1.2,1.5),(1.5 ,1.5),(1.5,1.2) ,(1.2,1.2)]
hole = [(1.2, 1.2),(1.2,1.5),(1.35,1.35), (1.5 ,1.5),(1.45,1.25),(1.5,1.2) ]
hole2t = np.array(hole)+0.45
hole2 = []
for i in range(len(hole2t)):
    hole2.append((hole2t[i][0],hole2t[i][1]))

hole3t = np.array(hole)+np.array([-0,0.45])
hole3 = []
for i in range(len(hole3t)):
    hole3.append((hole3t[i][0],hole3t[i][1]))

hole4t = np.array(hole)+np.array([0.35,0.1])
hole4 = []
for i in range(len(hole4t)):
    hole4.append((hole4t[i][0],hole4t[i][1]))

obstacles1= py2d.Math.Polygon.from_tuples(hole)
obstacles2= py2d.Math.Polygon.from_tuples(hole2)
obstacles3= py2d.Math.Polygon.from_tuples(hole3)
obstacles4= py2d.Math.Polygon.from_tuples(hole4)
#obstacles = [obstacles]
obstacles = []
#obstacles.append(obstacles1)
#obstacles.append(obstacles2)
##obstacles.append(obstacles3)
##obstacles.append(obstacles4)
##obstacles = [obstacles, obstacles2, obstacles3]


hole = np.array(hole)

t = np.array(t)
fig = plt.figure(facecolor='white')
plt.hold('on')
plt.plot(np.array(t[:,0]),np.array(t[:,1]),'r')
obstacles.append(obstacles1); plt.plot(np.array(hole[:,0]),np.array(hole[:,1]),'b',linewidth=3)
obstacles.append(obstacles2); plt.plot(np.array(hole2t[:,0]),np.array(hole2t[:,1]),'b',linewidth=3)
#obstacles.append(obstacles3); plt.plot(np.array(hole3t[:,0]),np.array(hole3t[:,1]),'b',linewidth=3)
#obstacles.append(obstacles4); plt.plot(np.array(hole4t[:,0]),np.array(hole4t[:,1]),'b',linewidth=3)

#%
result = pm.Polygon.convex_decompose(missionSpace,obstacles,debug_callback=True)
#fig = plt.figure(figsize=(10.5, 5.5),facecolor='white')

for i in range(len(result)):
    sub = []
    for j in range(len(result[i])):
        sub.append([result[i][j][0],result[i][j][1]])
    sub.append(sub[0])
    sub = np.array(sub)
    plt.plot(sub[:,0],sub[:,1])