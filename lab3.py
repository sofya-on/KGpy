# Пицхелаури С. Г. М8О-305Б-18
# 23. аппроксимация шарового слоя
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import tkinter as tk
from tkinter import Tk, StringVar, Entry, Button

#стороны 

def approximate(R,h,a):

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        phi = np.linspace(0, 2.0*np.pi, a+1)
        theta = np.linspace(0.75*np.pi, 0.6, a+1)

        x = R*np.outer(np.cos(phi), np.sin(theta))
        y = h*np.outer(np.sin(phi), np.sin(theta))
        z = np.outer(np.ones(np.size(phi)), np.cos(theta))

        ls = LightSource(azdeg=0, altdeg=65)
        rgb = ls.shade(y, plt.cm.RdYlBu)
        
        ax.set_title('Выполнила: Пицхелаури Софья (305Б) \n\n аппроксимация')

        ax.plot_surface(x, y, z, facecolors=rgb, alpha=0.9,linewidth=1)

        thet = np.linspace(0, 2.2* np.pi, 10)
        r = 0.9
        x = R*np.outer(np.cos(phi), np.sin(thet))
        y = h*np.outer(np.sin(phi), np.sin(thet))
        z = np.outer((r), (r))
        ax.plot_surface(x, y, z, rstride=4, cstride=4, color='w')

        t = np.linspace(0, 1.95* np.pi, 10)
        k = -0.8
        x = R*np.outer(np.cos(phi), np.sin(t))
        y = h*np.outer(np.sin(phi), np.sin(t))
        z = -1.* np.outer((k), (k))
        ax.plot_surface(x, y, z, rstride=4, cstride=4, color='w')


        ax.view_init(50.,60.)
        plt.show()

#построение

master = Tk()
greeting = tk.Label(text="Точность аппроксимации")
greeting.pack()

v = StringVar()
e = Entry(master, textvariable=v)
e.pack()
 
 
def get_value():
    approximate(1., 2.,int(v.get()))
 
 
def clean_value():
    v.set("")
 
b1 = Button(master, text="get value", width=10, command=get_value)
b2 = Button(master, text="clean", width=10, command=clean_value)
 
b1.pack()
b2.pack()
 
master.mainloop()



