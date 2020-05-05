# ECS152A Project 1: Discrete event simulation of Queue
## Description of discrete event simulation
Discrete event simulation is a method to simulate systems like a queue. Unlike synchronous simulation, discrete event simulation is based on the occurrence time of events instead of real time.  The simulation time jump from one event to next event. 
 
## Description of Project 1
This project is an implementation of discrete event simulation of a switch queue. We are able to simulate different situation by specifying different arrival rate of packets and service rate of packets.

## Overall Project Logic
### Data Structure
* Event: Event is a data structure to store an event. It includes timestamp and service time. 

* Global Event List (GEL) : Global Event list is a list to store every events generated in the simulation process. The data structure class is a subclass of LinkedList provided by Java.util package. Upon insertion, the newly added event will be inserted in a position to maintain a ascending order. 

* Packet Queue: Packet Queue is a queue to store each packet waiting for processing. The data structure class is a subclass of LinkedList provided by Java.util package. Besides the basic function of a queue, we add instance variable to record max queue size and implemente an 'add' method to drop packet if the queue has max queue size elements.


### Function
* Randdom Generator:  This function is to generate a random variable following an negative exponential distribution with a given rate. 

### Overall logic
The overall logic for the simulation is from assignment specification.

* Initialization: In initialization stage, global event list,  time, and packet queue will be initialzed. Also, the first arrival event will be generated with specified mu and lambda value. Moreover, variables to collect statistics are declared and initialized as well. 

* Event processing for Arrival event: This is the stage to process events. When an arrival event is processed, new arrival event will be put into the global event list. Then it will be processed if there is no packet processing. A departure event will be put into the global event list. If the processor is busy, then the packet will be inserted to a queue. 


* Event processing for Departure event: Departure event will be processed in this stage. If there are packets in queue, the first packet in the queue will be extracted and be put into global event list.

## Statistics Collection
* dropCount: This variable will be incremented by 1 when the queue size reaches the max buffer length.

* Utilization rate and BusyTime: BusyTime variable will be increament by service time of an arrival event when the arrival event is being processed. Eventually, utilization rate will be BusyTime divided by Time.

* MeanQueue length, arrivalCount and queueTotal: queueTotal will be increamented by length when an arrival event is being processed. Meanwhile, arrival counte will be incremented by 1. Eventually, MeanQueue length will be queueTotal divided by arrivalCount.

## Test Approach
we did both unit test and system test in this project.

* Unit test: we wrote three tests to check if all three data structures are working correctly.

* System test: we compare the output statistic with theoretical value to see if our simulation is working correctly.

## Project Insights and Individual contributions
### Yuliang Dong

 I have done the most coding implementation including data structures, overall logic and tests. In addition, I have done report except analysis part. Also, I have done shell script and python data processing.

In my opinion, the most challenging and interesting aspect of my implementation is learning discrete event simulation. Discrete event simulation is quite counter-intuitive to me who have lived in a world with linear time. However, I think it is a powerful tool for me to simulate the real world with higher efficiency. 