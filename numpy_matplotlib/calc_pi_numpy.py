import numpy as np
from scipy.spatial.distance import pdist, squareform

#number of points to use

n_pts=10000

pts=np.random.ranf((n_pts+1,2))
pts[0,...]=0.0
r=squareform(pdist(pts,"euclidean"))[:,0]
print("final pi est: "+str(4*sum(r<=1.0)/n_pts))
