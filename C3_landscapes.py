# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:37:22 2021
In this script we use an iterated function system to approximate the cantor set
C_3 and compute the persistence landscape at each iteration

@author: Lee
"""
from persim.landscapes import PersLandscapeApprox
from persim.landscapes import plot_landscape_simple
from persim.landscapes import plot_landscape
import numpy as np
import matplotlib.pyplot as plt
import scipy
#from scipy import ndimage
#import PIL
#from os import listdir
#from os.path import isfile, join
from persim import plot_diagrams

from ripser import ripser, lower_star_img
#from PersistenceLandscapeGrid import PersistenceLandscapeGrid
#from visualization import plot_landscape

#%%
def phi0(x):
    return x/3

def phi2(x):
    return (x+2)/3

#%% Chose a scale to compute the ifs up to 
#Keep the scale less than 30
scale = 3
C3prox = np.zeros(1)

for j in range(scale):
    out0 = phi0(C3prox)
    out2 = phi2(C3prox)
    C3prox = np.concatenate((out0, out2))
    print(max(C3prox))
    print(j)

print(np.sort(C3prox))

l = int(np.exp2(scale))
h = np.zeros(l)

#%% Plot the point in the scale:  

plt.figure(figsize = (10,8))
plt.scatter(C3prox, h)    
#plt.plot(years, y, "r--", lw = 5)
#plt.xlabel("year")
#plt.ylabel("tonnes per hectare")

#%% Compute the persistence landscape for the set
C3prox = np.reshape(C3prox, [l,1])
h = np.reshape(h, [l,1])
C3prox = np.concatenate((C3prox, h), axis = 1)
Dgmprox = ripser(C3prox, maxdim = 1)['dgms']
plot_diagrams(Dgmprox, show=True, lifetime = True)

#%%
Landprox = PersLandscapeApprox(dgms=Dgmprox, hom_deg=0)
#Landprox.compute_landscape()
ttl = "PL for scale " + str(scale)
plot_landscape_simple(landscape=Landprox, title = ttl)
#%% We repeat what we did for the cantor set with a different IFS in 2-dimensions
def phi0(x):
    return x/3

def phi20(x):
    return (x+np.array([2,0]))/3
def phi02(x):
    return (x+np.array([0,2]))/3
#%% Chose a scale to compute the ifs up to 
#Keep the scale less than 30
scale = 3
SArray = np.array([[0,0],[1,0],[0,1]])

for j in range(scale):
    out0 = phi0(SArray)
    out20 = phi20(SArray)
    out02 = phi02(SArray)
    SArray = np.concatenate((out0, out20, out02), axis = 0)
    print(j)

print(SArray)

#%% Plot at scale
plt.figure(figsize = (10,10))
plt.scatter(SArray[:,0], SArray[:,1])    
#%%
Dgmprox = ripser(SArray, maxdim = 1)['dgms']
plot_diagrams(Dgmprox, show=True, lifetime = False)
print(Dgmprox)
#%%
Landprox = PersLandscapeApprox(dgms=Dgmprox, hom_deg=0)
#Landprox.compute_landscape()
ttl = "PL for scale " + str(scale)
#plot_landscape(landscape=Landprox, title = ttl)
plot_landscape(landscape=Landprox)

#%% We add one more function to the IFS for 2-dim, giving us C3xC3
def phi21(x):
    return (x+np.array([2,1]))/3
def phi01(x):
    return (x+np.array([0,1]))/3

#%%#%% Chose a scale to compute the ifs up to 
#Keep the scale less than 30
scale = 2
SArray = np.array([[0,0],[1,0],[0,0.5],[1,0.5]])

for j in range(scale):
    out0 = phi0(SArray)
    out20 = phi20(SArray)
    out02 = phi01(SArray)
    out22 = phi21(SArray)
    SArray = np.concatenate((out0, out20, out02, out22), axis = 0)
    print(j)

print(SArray)
#%% Plot at scale
plt.figure(figsize = (10,5))
plt.scatter(SArray[:,0], SArray[:,1], s = .1)    
#%%
Dgmprox = ripser(SArray, maxdim = 0)['dgms']
plot_diagrams(Dgmprox, show=True, lifetime = False)
print(Dgmprox)

#%%
Landprox = PersLandscapeApprox(dgms=Dgmprox, hom_deg=0)
#Landprox.compute_landscape()
ttl = "PL for scale " + str(scale)
plot_landscape_simple(landscape=Landprox, title = ttl)