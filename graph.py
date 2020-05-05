from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

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


def my_graph(start, end, buffersize):
	# data obtained from main.java
	ld = np.array([0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 0.9, 0.2, 0.4, 0.5, 0.6, 0.8, 0.9, 0.2, 0.4, 0.5, 0.6, 0.8, 0.9, 0.2, 0.4, 0.5, 0.6, 0.8, 0.9])
	maxbuffer = np.array([-1, -1,-1,-1,-1,-1,-1,1,1,1,1,1,1,20,20,20,20,20,20,30,30,30,30,30,30,])
	drop = np.array([0,0,0,0,0,0,0,1737,5387,7575, 10369,15024,17575, 0,0,0,0,81,727,0,0,0,0,5,220])
	mean_queue = np.array([0.11142,0.245315,0.67566,0.98804,1.463251, 4.18326, 8.207232, 0.231674, 0.461571, 0.567896, 0.681055, 0.84986, 0.927791, 0.24822, 0.668407, 1.00688, 1.57174, 3.663989, 6.800433, 0.24536, 0.68784, 1.00826, 1.538089, 4.137769, 7.768577])
	utilizatio_rate = np.array([0.100774, 0.199309, 0.399479, 0.501785, 0.5952, 0.795634, 0.898451, 0.204953, 0.40092, 0.49853, 0.608637, 0.796405, 0.895581, 0.199073, 0.40126, 0.503206, 0.606748, 0.798178, 0.898606, 0.199022, 0.406016, 0.503396, 0.598665, 0.804323, 0.896989])
	u = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
	# plot practical mean queue length
	plt.figure()
	plt.plot(ld[start: end], mean_queue[start: end], '-x')
	plt.ylabel("mean queue length")
	plt.xlabel("lambda")
	plt.title("buffer size is " + str(buffersize))
	# plot theoretical mean queue length
	plt.figure()
	plt.plot(ld[start:end], avg_cust_calculator(ld[start:end], u[start:end], (end - start)), '-x')
	plt.ylabel("theoretical mean queue length")
	plt.xlabel("lambda")
	plt.title("buffer size is " + str(buffersize))
	# plot practical utilization rate
	plt.figure()
	plt.plot(ld[start:end], utilizatio_rate[start:end], '-x')
	plt.ylabel("utilization rate")
	plt.xlabel("lambda")
	plt.title("buffer size is " + str(buffersize))
	# plot practical utilization rate
	plt.figure()
	plt.plot(ld[start:end], avg_ut_calculator(ld[start:end], u[start:end], (end - start)), '-x')
	plt.ylabel("theoretical utilization rate")
	plt.xlabel("lambda")
	plt.title("buffer size is " + str(buffersize))
	# plot practical drop count
	plt.figure()
	plt.plot(ld[start:end], drop[start:end], '-x')
	plt.ylabel("drop count")
	plt.xlabel("lambda")
	plt.title("buffer size is " + str(buffersize))
	
	
def main():
	my_graph(0, 7, -1)
	my_graph(7, 13, 1)
	my_graph(13, 19, 20)
	my_graph(19, 25, 30)
	plt.show()
	
	
if __name__ == "__main__":
	main()