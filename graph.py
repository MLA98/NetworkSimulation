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
	#extra credit
	extra_drop = [0,0,0,0,0,0,0,6759,2781,1239,457,3,0,3,0,0,0,0,0,0,0,0,0,0,0]
	extra_mean = [4.304768,1.598548,0.486460,0.258280,0.116458,0.007340,0.000120,0.573567,0.335175,0.208653,0.114516,0.007140,0.00006,1.771349,0.47617,0.2616,0.1174,0.0069,0.00006,1.685059,0.459060,0.250435,0.119240,0.006640,0.00006]
	extra_ut = [0.900137,0.793716,0.603820,0.502276,0.397040,0.198099,0.100764,0.800278,0.604595,0.497766,0.401754,0.199603,0.100919,0.799526,0.597811,0.500953,0.396742,0.199702,0.101096,0.79919,0.597122,0.498385,0.399929,0.200821,0.099931]
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
	#extra credit
	plt.figure()
	plt.plot(ld[start: end], extra_mean[start: end], '-x')
	plt.ylabel("mean queue length")
	plt.xlabel("lambda")
	plt.title("(extra credit) buffer size is " + str(buffersize))
	
	plt.figure()
	plt.plot(ld[start:end], extra_ut[start:end], '-x')
	plt.ylabel("utilization rate")
	plt.xlabel("lambda")
	plt.title("(extra credit) buffer size is " + str(buffersize))
	
	plt.figure()
	plt.plot(ld[start:end], extra_drop[start:end], '-x')
	plt.ylabel("drop count")
	plt.xlabel("lambda")
	plt.title("(extra credit) buffer size is " + str(buffersize))


	
	
	
def main():
	my_graph(0, 7, -1)
	my_graph(7, 13, 1)
	my_graph(13, 19, 20)
	my_graph(19, 25, 30)
	plt.show()
	
	
if __name__ == "__main__":
	main()