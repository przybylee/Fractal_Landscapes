# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 16:37:34 2021

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
C3prox = np.array([0,1])

for j in range(scale):
    out0 = phi0(C3prox)
    out2 = phi2(C3prox)
    C3prox = np.concatenate((out0, out2))
    #print(max(C3prox))
    print(j)

print(np.sort(C3prox))

l = int(np.exp2(scale+1))
h = np.zeros(l)

#%% Plot the point in the scale:  

plt.figure(figsize = (12,1))
plt.scatter(C3prox, h, linewidth = .1)  
plt.text(0.5, -.01, "$S_n$", size= 15)
plt.yticks([])  
#plt.plot(years, y, "r--", lw = 5)
#plt.xlabel("year")
#plt.ylabel("tonnes per hectare")
#%% Plot the point in the scale:  
out0 = phi0(C3prox)
out2 = phi2(C3prox)
Snplus1 = np.concatenate((out0, out2))
hplus = np.zeros(2*l)
fig, (ax1,ax2) = plt.subplots(2, figsize=(12,1), sharex= True)
ax1.scatter(C3prox, h, linewidth = 0.1)
#ax1.title = "$S_n$"
ax2.scatter(out0, h, linewidth = .1, color = "green")  
ax2.scatter(out2, h, linewidth = .1, color = "red")  
#ax2.scatter(Snplus1, hplus, linewidth = .1)
ax2.text(0.16, -.01, "$L_n$", size= 15)
ax2.text(0.82, -.01, "$R_n$", size= 15)
ax1.text(0.5, -.01, "$S_n$", size= 15)
#ax2.text(0.5, -.01, "$S_{n+1}$", size= 15)
ax1.set_yticks([]) 
ax2.set_yticks([]) 

#%% Here is the modified 1/5 example
def psi0(x):
    return x/5

def psi1(x):
    return (x+1)/5

def psi4(x):
    return (x+4)/5

#%% Chose a scale to compute the ifs up to 
#Keep the scale less than 30
scale = 4
Att_prox = np.array([0,1])

for j in range(scale):
    out0 = psi0(Att_prox)
    out1 = psi1(Att_prox)
    out4 = psi4(Att_prox)
    Att_prox = np.concatenate((out0, out1, out4))
    #print(max(C3prox))
    print(j)

print(np.sort(Att_prox))

l = len(Att_prox)
h = np.zeros(l)

#%% Plot the point in the scale:  
hminus = np.zeros(len(out0))
plt.figure(figsize = (12,1))
plt.scatter(Att_prox, h, linewidth = .1)  
plt.scatter(out0, hminus, color = "red", linewidth = .1)  
plt.scatter(out1, hminus, color = "blue", linewidth = .1)
plt.scatter(out4, hminus, color = "green", linewidth = .1)
plt.scatter(0.2, 0, color = "purple", linewidth = .1)
plt.text(0.5, -.01, "$S_n$", size= 15)
plt.yticks([])  

#%% Plot the point in the scale:  
out0 = psi0(Att_prox)
out1 = psi1(Att_prox)
out4 = psi4(Att_prox)
Snplus1 = np.concatenate((out0, out1, out4))
hplus = np.zeros(len(Snplus1))
fig, (ax1,ax2) = plt.subplots(2, figsize=(12,1), sharex= True)
ax1.scatter(Att_prox, h, linewidth = 0.1)
#ax1.title = "$S_n$"
ax2.scatter(out0, h, linewidth = .1, color = "red")  
ax2.scatter(out1, h, linewidth = .1, color = "blue")
ax2.scatter(out4, h, linewidth = .1, color = "green")  
ax2.scatter(0.2, 0, linewidth = .1, color = "purple")
ax2.text(0.5/5, -.01, "$K_1$", size= 15)
ax2.text(0.31, -.01, "$K_2$", size= 15)
ax2.text(0.91, -.01, "$K_3$", size= 15)
ax1.text(0.5, -.01, "$S_n$", size= 15)
ax2.text(0.5, -.01, "$S_{n+1}$", size= 15)
ax1.set_yticks([]) 
ax2.set_yticks([]) 

#%% Compute the persistence landscape for the set
Att_prox = np.reshape(Att_prox, [l,1])
Dgmprox = ripser(Att_prox, maxdim = 0)['dgms']
plot_diagrams(Dgmprox, show=True, lifetime = True)
print(Dgmprox)
#%%
Landprox = PersLandscapeApprox(dgms=Dgmprox, hom_deg=0)
#Landprox.compute_landscape()
ttl = "PL for scale " + str(scale)
plot_landscape(landscape=Landprox, title = ttl)

#%% Plot a simple version of the landscape, this is faster
plot_landscape_simple(landscape = Landprox, title = ttl)

#%% Now we consider the Cantor triangle example
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
plt.figure(figsize = (5,5))
# Color the shape
x = SArray[:,0]
y = SArray[:,1]
plt.scatter(SArray[:,0], SArray[:,1],linewidth = .1, Color = "blue", zorder = 2)  
plt.title("$S_3$", size = 20)
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
