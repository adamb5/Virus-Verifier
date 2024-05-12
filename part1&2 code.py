//SEIR vs time. When is the peak of infected people reached? What is the maximum number of infected people?

import numpy as np
from matplotlib import pyplot as plt

def f(r):
    beta    = 0.75     
    mu      = 1/(83.*365) 
    gamma   = 1./8.        
    epsilon = 1./3. 
    alpha   = 0.006
    xs=r[0]
    xe=r[1]
    xi=r[2]
    xr=r[3] 
    xn=xs+xe+xi+xr
    fs= - beta * xs * xi / xn - mu * xs + mu * xn
    fe=   beta * xs * xi / xn - ( mu + epsilon ) * xe
    fi=   epsilon * xe - ( gamma + mu + alpha ) * xi
    fr=   gamma * xi - mu*xr
    return np.array([fs,fe,fi,fr],float)

n0 =10000000
ne0=20000
ni0=1
r=np.array([n0-ne0-ni0,ne0,ni0, 0],float) 

nstep = 1000
t = np.linspace(0, 300., nstep)
h = t[1]-t[0]

xs=np.zeros(nstep)
xe=np.zeros(nstep)
xi=np.zeros(nstep)
xr=np.zeros(nstep)

xfs =np.zeros(nstep)
xfe =np.zeros(nstep)
xfi =np.zeros(nstep)
xfr =np.zeros(nstep)



for i in range(nstep):
        xs[i]=r[0]
        xe[i]=r[1]
        xi[i]=r[2]
        xr[i]=r[3]
        k1=h*f(r)
        k2=h*f(r+0.5*k1)    
        r+=k2

        xf=f(r)
        xfs[i]=xf[0]
        xfe[i]=xf[1]
        xfi[i]=xf[2]
        xfr[i]=xf[3]
    
xdn = n0  - ( xs + xe + xi + xr )
    
plt.plot(t,xs,label="S")
plt.plot(t,xe,label="E")
plt.plot(t,xi,label="I")
plt.plot(t,xr,label="R")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend(loc="best")
plt.xlabel(r'$t$ (days)',fontsize=20) 
plt.ylabel(r'population',fontsize=20)
plt.show()

xd = - ( xfs + xfe + xfi + xfr )

plt.plot(t, xd,label="deaths per day")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend(loc="best")
plt.xlabel(r'$t$ (days)',fontsize=20) 
plt.ylabel(r'deaths per unit time',fontsize=20)
plt.show()
plt.plot(t, xr/390000,label="death rate")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend(loc="best")
plt.xlabel(r'$t$ (days)',fontsize=20) 
plt.ylabel(r'dead individuals',fontsize=20)
plt.show()
