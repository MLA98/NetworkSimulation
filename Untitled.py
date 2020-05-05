from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline

def avg_cust_calculator(ld, u, l):
	result = []
	for i in range(l):
		p = ld[i]/u[i]
		result.append(p/(1-p))
	return result	

def avg_ut_calculator(ld, u, l):
	result = []
	for i in range(l):
		p = ld[i]/u[i]
		result.append(p)
	return result	


ld = np.array([0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 0.9, 0.2, 0.4, 0.5, 0.6, 0.8, 0.9, 0.2, 0.4, 0.5, 0.6, 0.8, 0.9, 0.2, 0.4, 0.5, 0.6, 0.8, 0.9])
#ld = np.array(ld)

maxbuffer = np.array([-1, -1,-1,-1,-1,-1,-1,1,1,1,1,1,1,20,20,20,20,20,20,30,30,30,30,30,30,])
#maxbuffer = np.array(maxbuffer)

drop = np.array([0,0,0,0,0,0,0,1737,5387,7575, 10369,15024,17575, 0,0,0,0,81,727,0,0,0,0,5,220])
#drop = np.array(np)

mean_queue = np.array([0.11142,0.245315,0.67566,0.98804,1.463251, 4.18326, 8.207232, 0.231674, 0.461571, 0.567896, 0.681055, 0.84986, 0.927791, 0.24822, 0.668407, 1.00688, 1.57174, 3.663989, 6.800433, 0.24536, 0.68784, 1.00826, 1.538089, 4.137769, 7.768577])
#mean_queue = np.array(mean_queue)

utilizatio_rate = np.array([0.100774, 0.199309, 0.399479, 0.501785, 0.5952, 0.795634, 0.898451, 0.204953, 0.40092, 0.49853, 0.608637, 0.796405, 0.895581, 0.199073, 0.40126, 0.503206, 0.606748, 0.798178, 0.898606, 0.199022, 0.406016, 0.503396, 0.598665, 0.804323, 0.896989])

u = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

#plt.plot(ld[19:25], mean_queue[19:25], '-x')
#plt.ylabel("mean queue length")
#plt.xlabel("lambda")
#plt.title("buffer size is 30")
#plt.show()

#print(avg_cust_calculator(ld[7:13], u[7:13], 6))
#plt.plot(ld[19:25], avg_cust_calculator(ld[19:25], u[19:25], 6), '-x')
#plt.ylabel("theoretical mean queue length")
#plt.xlabel("lambda")
#plt.title("buffer size is 30")
#plt.show()

#
plt.plot(ld[19:25], avg_ut_calculator(ld[19:25], u[19:25], 6), '-x')
plt.ylabel("theoretical utilization rate")
plt.xlabel("lambda")
plt.title("buffer size is 20")
plt.show()



#plt.plot(ld[19:25], drop[19:25], '-x')
#plt.ylabel("drop count")
#plt.xlabel("lambda")
#plt.title("buffer size is 30")
#plt.show()

#plt.plot(ld[19:25], utilizatio_rate[19:25], '-x')
#plt.ylabel("utilization rate")
#plt.xlabel("lambda")
#plt.title("buffer size is 30")
#plt.show()


#plt.plot(ld[8:13], mean_queue[8:13], '-x')
#plt.ylabel("mean queue length")
#plt.xlabel("lambda")
#plt.title("buffer size is infinite")
#plt.show()