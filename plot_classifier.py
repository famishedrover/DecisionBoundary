import numpy as np
import matplotlib.pyplot as plt
class plot_classifier :

	def __init__ (self , classifier ) :
		self.classifier = classifier
		self.k = None
		self.pred = None
		self.left = None
		self.right = None

	def getGrid(self , left = -1.0, right = 1.0 , step = 0.01) :
		self.left = left
		self.right = right
		x = np.arange(left , right , step)
		z = np.meshgrid(x,x)
		k = np.c_[z[0].ravel(),z[1].ravel()]
		print 'Shape of Grid :',k.shape
		self.k = k
		print 'Grid Created.'

	def getPredictionOnGrid (self) :
		clf = self.classifier
		pred = clf.predict(self.k)
		self.pred = pred
		print pred.mean()


	def plotBoundaries(self) :
		plt.figure(6)
		plt.xlim(self.left,self.right)
		plt.ylim(self.left,self.right)
		for ix in range(self.k.shape[0]) :
			if self.pred[ix] == 0 :
				plt.scatter(self.k[ix,0] , self.k[ix,1] ,linewidths=10, color = 'green' )
			else :
				plt.scatter(self.k[ix,0] , self.k[ix,1] ,linewidths=10, color = 'red' )
		plt.show()

if __name__ == "__main__" :
	p = plot_classifier(1)

	# ! ! ! train the classifier with normalised data ! ! ! 


	p.getGrid(step = 0.5)
	for ix in p.k :
		print ix











