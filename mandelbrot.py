#!/usr/bin/env python
# coding: utf-8

# In[48]:


def mandelbrot(n, N_max, threshold):
    """
    Computes the Mandelbrot fractal with an input of threshold, 2d array dimensions, and a maximum N value.
    Produces a plot of the Mandelbrot fractal as the output.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.linspace(-2, 1, n)
    y = np.linspace(-1.5, 1.5, n)
    xx, yy = np.meshgrid(x, y)
    c = xx + yy * 1j #starting here to end of function is a reapplication of the code provided in the original HW4 pdf
    z = 0
    for j in range (N_max):
        z = z ** 2 + c
    #two runtime warnings produced here, has no effect on the result so it is safe to ignore    
    mask = abs(z) < threshold
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png') #The Mandelbrot fractal output in the form of a figure as a png

#User input for the three values, for simple ease of use without needing to change the code to test different values
n = int(input("Enter n value: "))
N_max = int(input("Enter N_max: "))
threshold = int(input("Enter threshold: "))
mandelbrot(n, N_max, threshold)

#Some combination results that I found
#Making every input 100 will make a similar shape to the example but rotated -90 degrees, and without a line at the end
#When made 200 for all, same thing but the imagine produced definitely seemed more clearer on the edges
#The higher you make the number, the more "defined" the edges get it seems.
#Of interesting note, if you were to put a low value(say 1) as the value of threshold but N_max and n value were high values
#(200 for example), the plot is still essentially the same, but should either of those values be lower, the graph would change
#into having no white part. This implies that threshold isn't as essential of a factor as the others.

