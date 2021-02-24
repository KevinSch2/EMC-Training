#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import basic librarys 
import numpy as np #is used for mathematical formulas
import matplotlib.pyplot as plt # is used for plot grafics


#Time [ms] simulation    
T = 20 
#Number of samples
N = 100
#Time [ms] for Plot    
t=np.linspace(0,T,N*T)

#Define sinus funktion amplidude[x], frequency[Hz], angle in [degree], order[1,2,3,...,n]
def sin(a,f,angle_deg,k):
    phi=angle_deg*(np.pi/180)
    x=a*np.sin(2*np.pi*f*k*t/1000+phi*k)
    return x


#Define Plot 
def graph(x,legend):
    plt.plot(t,x,linewidth=2, label=legend)

#Define Grid for PLots  
def grid():
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    plt.grid(b=True, color='black', linestyle='-',alpha=0.1)
    plt.xlim(0, T)
    plt.ylabel(r'$\hat x$ [Amplitude]', fontsize='x-large')
    axes1 = plt.gca()
    axes1.set_xlabel("t [Time in ms]", fontsize='x-large')  
    


# In[2]:


'''
####dictionary####

#Sinus like this
y=sin(230,50,45,1)

#Basic polt
graph('funktion','legend')

#Basic plot title
plt.title('Sinus Funkion',fontsize='x-large')

#print plot
plt.show()
'''
  


# In[3 ]:


#example Sinus
fx=sin(1,50,0,1) #use funktion (x=1, f=50Hz,phi=0°,1st Order)
graph(fx,"Sinus")#use funktion for generating a graph
plt.show()       #show the plot


# In[4 ]:
%load_ext watermark

# python, ipython, packages, and machine characteristics
%watermark -v -m -p pandas,numpy,matplotlib.pyplot,watermark 

# date
print (" ")
%watermark -u -n -t -z 