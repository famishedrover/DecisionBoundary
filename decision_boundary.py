from sklearn.tree import DecisionTreeClassifier
from dummy_data_set import dist
from plot_classifier import plot_classifier
import numpy as np
m1 = [6.0,5.0]
m2 = [8.0,8.5]
c1 = [[2.0,0.4],[0.4,1.0]]
c2 = [[1.0,0.0],[0.0,4.0]]


d = dist(m1,m2,c1,c2,size = 500)
d.getDist()
d.getLabels()
d.plotDist()

data = d.data
labels = d.labels
all_data = np.zeros((data.shape[0],data.shape[1] + 1))
all_data[:, :data.shape[1]] = data 
all_data[:,-1] = labels
# np.random.shuffle(all_data)
left = all_data[:,0].argmax()
right = all_data[:,1].argmax()
left = all_data[left,0]
right = all_data[right,1]
print 'all_data :' , all_data.shape
print left 
left = -1.0*left
print right

# all_data[:,0] = all_data[:,0]/left + 0.0000000001
# all_data[:,1] = all_data[:,1]/right + 0.0000000001

# left = all_data[:,0].argmax()
# right = all_data[:,1].argmax()
# left = all_data[left,0]
# right = all_data[right,1]
# print 'New :'
# print left
# print right 

clf = DecisionTreeClassifier()
clf.fit(all_data[:,:-1],all_data[:,-1])



p = plot_classifier(clf)
p.getGrid(left,right,step=0.5)
p.getPredictionOnGrid()
p.plotBoundaries()








