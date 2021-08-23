# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 13:30:54 2021

@author: Lee

Plot triangle example of Cech complex
"""
import numpy as np
import matplotlib.pyplot as plt
from persim.landscapes import PersLandscapeApprox
from persim.landscapes import plot_landscape_simple
from persim.landscapes import plot_landscape
from persim import plot_diagrams
from ripser import ripser, lower_star_img

#%% Plot triangle
x = [0,1,1/2]
y = [0,0,np.sqrt(3)/2]

#create a figure
#plt.figure(figsize = (10,10))
fig,ax = plt.subplots(1)
ax.set_aspect("equal")
ax.scatter(x,y, zorder = 2)
#ax.scatter(0.5,np.sqrt(3)/6, color= 'r', zorder = 2)
#plt.axis("off")
plt.title("Data:  $X$")
plt.show()

#%% blow up points

#create a figure
#plt.figure(figsize = (10,10))
fig,ax = plt.subplots(1)
ax.set_aspect("equal")
ax.scatter(x,y, zorder = 2)
#ax.scatter(0.5,np.sqrt(3)/6, color= 'r', zorder = 2)
rad = 0.55
for j in range(3):
    circ = plt.Circle((x[j],y[j]), rad)
    ax.add_patch(circ)
#plt.axis("off")
title = "radius = " + str(rad) + "$< 3^{-1/2}$"
plt.title(title)
plt.show()
#%% Vietoris Rips Complex
plt.scatter(x, y)
#create a figure
#plt.figure(figsize = (10,10))
fig,ax = plt.subplots(1)
ax.set_aspect("equal")
ax.scatter(x,y, color = "blue", zorder = 2)
ax.fill(x,y, facecolor = "blue", edgecolor = "blue", linewidth = 3)
#ax.scatter(0.5,np.sqrt(3)/6, color= 'r', zorder = 2)
plt.axis("off")
plt.title("VR$(X,0.1.1)$")
plt.show()

#%% Cech complex
plt.scatter(x, y)
#create a figure
#plt.figure(figsize = (10,10))
fig,ax = plt.subplots(1)
ax.set_aspect("equal")
ax.scatter(x,y, color = "blue", zorder = 2)
ax.fill(x,y, facecolor = "none", edgecolor = "blue", linewidth = 3)
#ax.scatter(0.5,np.sqrt(3)/6, color= 'r', zorder = 2)
plt.axis("off")
plt.title("Cech$(X,0.1.1)$")
plt.show()

#%% Here is an example for a persistence module
# Plot data

data = np.array([[0,0], [0,.6], [0.5,0.8], [0.8,0], [0.2,1]])
N = np.shape(data)[0]
x = data[:,0]
y = data[:,1]
#create a figure
#plt.figure(figsize = (10,10))
fig,ax = plt.subplots(1)
ax.set_aspect("equal")
ax.scatter(x,y, zorder = 2)
#ax.scatter(0.5,np.sqrt(3)/6, color= 'r', zorder = 2)
#plt.axis("off")
plt.title("Data:  $X$")
plt.show()

#%%
Dgmprox = ripser(data, maxdim = 1)['dgms']
plot_diagrams(Dgmprox, show=True, title = "VR persistence diagram" )
print(Dgmprox)

#%% blow up points

#create a figure
fig,ax = plt.subplots(1)
ax.set_aspect("equal")
ax.scatter(x,y, zorder = 2)
#ax.scatter(0.5,np.sqrt(3)/6, color= 'r', zorder = 2)
eps = 0.9
for j in range(5):
    circ = plt.Circle((x[j],y[j]), eps/2)
    ax.add_patch(circ)
#plt.axis("off")
title = "r = " + str(eps) 
plt.title(title)
plt.show()
#%% Draw the corresponding simplicial complex for r
eps = 0.7
#connections = np.zeros([N,N])
#fig,ax = plt.subplots(1)
plt.figure(figsize = (10,10))
#plt.set_aspect("equal")
plt.scatter(x,y, zorder = 2)
for j in range(N):
    for k in range(j,N):
        if (j !=k):
            xj = data[j]
            xk = data[k]
            dist = np.linalg.norm(xj-xk)
            if (dist < eps):
                xvalues = [xj[0], xk[0]]
                yvalues = [xj[1], xk[1]]
                plt.plot(xvalues,yvalues, color = "blue")
                for l in range(k+1,N):
                    xl = data[l]
                    dist = np.linalg.norm(xj-xl)
                    if (dist < eps):
                        dist = np.linalg.norm(xk-xl)
                        if (dist <eps):
                            xvalues = data[[j,k,l],0]
                            yvalues = data[[j,k,l],1]
                            plt.fill(xvalues,yvalues, color = "lightblue")
titl = "VR$(X,$" + str(eps) + ")"
plt.title(titl, size = 20)
plt.show()

#%% Plot a barcode manually
eps = 1.0
lwidth = 17
plt.figure(figsize=(10,10))
x = Dgmprox[0][0]
y = [0,0]
plt.plot(x,y, color = "blue", lw = lwidth, label = "$H_0$")
for j in range(1,N-1):
    x = Dgmprox[0][j]
    y = [0.1*j,0.1*j]
    plt.plot(x,y, color = "blue", lw = lwidth)
x = [0,1.5]
y = [0.1*4,0.1*4]
#plt.plot(x,y, color = "blue", lw = lwidth)
plt.arrow(0,0.4, 1.4, 0, color = "blue", lw = lwidth, head_length = 0.015, head_width = 0.01)
x = Dgmprox[1][0]
y = [-0.1,-0.1]
plt.plot(x,y, color = "green", lw = lwidth, label = "$H_1$")
plt.legend(loc = 4, prop = {'size': 25})
yticks = [-0.1, 0, 0.1, 0.2, 0.3, 0.4]
plt.yticks([])
vx = [eps,eps]
vy = [-0.15,0.45]
plt.plot(vx,vy, color = "red", linestyle = "--")
#plt.show()
titl = "Ex2Barcode" + str(eps)+ ".png"
#plt.savefig("Ex2Barcode.png")
plt.savefig(titl)
#%% Save the plot
#Make sure to go to the correct working directory first
titl = "Ex2Barcode" + str(eps)+ ".png"
plt.savefig(titl)