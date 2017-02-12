import numpy as np
class dist :
	def __init__ (self , mean1 = [-1.5,4.0] , mean2 = [-1.0,-1.0], cov1 = [[1.0,0.0],[0.0,1.0]], cov2 = [[0.9,0.3],[0.3,0.9]], size = 50) :
		self.mean1 = mean1
		self.mean2 = mean2
		self.cov1 = cov1
		self.cov2 = cov2
		self.size = size 
		self.dist_01 = None
		self.dist_02 = None
		self.data = None
		print 'Dist Created.'

	def getDist(self) :
		mean_01 = np.array(self.mean1)
		mean_02 = np.array(self.mean2)

		cov_01 = np.array(self.cov1)
		cov_02 = np.array(self.cov2)
		size = self.size
		dist_01 = np.random.multivariate_normal(mean_01, cov_01 , size)
		dist_02 = np.random.multivariate_normal(mean_02, cov_02 , size)
		data = np.zeros((dist_01.shape[0] + dist_02.shape[0] , dist_01.shape[1]))
		data[:dist_01.shape[0]] = dist_01
		data[dist_01.shape[0] : ] = dist_02
		print 'data.shape :',data.shape
		print 'dist_01.shape :',dist_01.shape
		self.data = data
		self.dist_01 = dist_01
		self.dist_02 = dist_02
		print 'Dist Generated.'
	
	def plotDist(self) :
		if self.dist_01 is  None or self.dist_02 is  None :
			print 'No distributions Found !'
		else :
			import matplotlib.pyplot as plt
			print 'dist_01 :','red'
			print 'dist_02 :','green'
			plt.scatter(self.dist_01[:,0] , self.dist_01[:,1] , color = 'red')
			plt.scatter(self.dist_02[:,0] , self.dist_02[:,1] , color = 'green')
			plt.show()
			print 'Dist Plotted.'

if __name__ == "__main__" :
	d = dist(size = 5000)
	d.getDist()
	d.plotDist()
