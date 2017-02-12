# # 

# import numpy as np
# import matplotlib.pyplot as plt
# r = 1.0
# step = 0.01
# x = np.arange(-1.0*r , r , step)
# z = np.meshgrid(x,x)
# print z[0].shape
# print z[1].shape

# k0 = z[0].ravel()
# k1 = z[1].ravel()

# k = np.c_[k0,k1]
# print k.shape

# plt.figure(0)
# plt.xlim(-1.0*r , r)
# plt.ylim(-1.0*r , r)

# plt.scatter(k[:k.shape[0]/2, 0] , k[:k.shape[0]/2 ,1] , linewidths = 0.1 , color = 'r')

# plt.scatter(k[k.shape[0]/2 : , 0] , k[k.shape[0]/2 : ,1] , linewidths = 0.1)
# plt.show()
# # import numpy as np
# # z = np.zeros((5,5))
from dummy_data_set import dist

d = dist()
d.getDist()
d.plotDist()

