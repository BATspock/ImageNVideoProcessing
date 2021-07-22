import numpy as np
import matplotlib.pyplot as plt

phi = np.random.randn(20, 20) #provide initial value for phi function
F =  #define force function for the image
dt = 1
it = 100 

for i in range(it):
    dphi = np.gradient(phi)
    dphi_norm = np.sqrt(np.sum(dphi**2, axis=0))

    phi += dt * F * dphi_norm

    plt.contour(phi, 0)
    plt.show()