import numpy as np
import math as m
import matplotlib.pyplot as mp
import sympy as sp
import sraices as sr
 
#%%
x=np.arange(-5,5,0.1)
y=x-np.power(2,-x)
f=mp.plot(x,y) 
mp.grid(True)
mp.axis([-2,2,-5,1])
mp.show()

#%%
x=sp.symbols('x')
y=sp.sin(x/2)-5*sp.exp(-x)
sp.plotting.plot(y,(x,1.5,2))
sr.secante(y,0,1,1e-3)
