import numpy as np
#number of points to use
n_pts=100000
pts=np.random.ranf((n_pts,2))
r = np.sum(pts*pts,axis=1)
print("final pi est: "+str(4*sum(r<=1.0)/n_pts))
