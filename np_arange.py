import numpy as np
z = [1,2,3,4]

x = np.arange(-2.0,3.0,2)
y = np.arange(3.0,8.0 ,2)
print 'y \n',y
print 'x \n' ,x
print 'z '
z = np.meshgrid(x,y)
for zx in z :
	print zx


k = z[0].ravel()
k1 = z[1].ravel()
print 'k \n',k
print 'k1 \n',k1

k2 = np.c_[k , k1]
l = [k,k1]
# print 'l \n',l
print 'l '
for lx in l :
	print lx


print 'k2 \n',k2
# print 'z[0] ',z[0]
# q = z[0].ravel()
# print 'q ', q