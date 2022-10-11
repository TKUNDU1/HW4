#!/usr/bin/env python
# coding: utf-8

# In[61]:


import numpy as np
import matplotlib.pyplot as plt
def markov(n, N):
    """
    Produces the plot of the norm of the difference between a varying probability distribution that varies between iterations 
    and a static probability distribution, against the iterations.
    Requires input of the array size n, and the number of iterations N.
    """
    p = np.random.rand(n, 1)
    rowsum = np.sum(p)
    p = p/rowsum #the code in place to make sure rows add up to 1 despite being randomly generated.
    P = np.random.rand(n, n)
    for i in range(n):
        rowsum = np.sum(P[i])
        P[i] = P[i]/rowsum
    normarray = []
    evalue, evector = np.linalg.eig(np.transpose(P))
    for i in range(N):
        p = np.dot(np.transpose(P), p)
        u = evector[np.argmax(evalue)]
        rowsum = np.sum(u)
        p_stationary = u/rowsum
        normarray.append(np.linalg.norm(p - p_stationary)) #an array recording various norms of different iterations
    z = list(range(1, N+1))
    plt.plot(z, normarray)
n = int(input("Enter n value: ")) #user input system for ease of use
N = int(input("Enter N value: "))
markov(n, N)

#Result comments
#When testing the graph of n=5, N=50, I noticed the model would come out in one of two ways. The graph would either rapidly 
#upwards or downwards in the first few iterations, and then the difference would remain incredibly constant for the rest of the
#iterations, after stabilizing. Something I noticed was that when I varied the input, the more N was larger then n, the more
#rapidly it would achieve its constant point. If n was larger then N, it would take more portion of the graph and more slowly
#achieve this constant value for the rest of the iterations, making the increase/decrease portion of the plot less steep.

