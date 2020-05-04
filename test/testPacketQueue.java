package test;

import static org.junit.jupiter.api.Assertions.*;

import java.util.LinkedList;
import java.util.Queue;

import org.junit.jupiter.api.Test;

import proj1.PacketQueue;

class testPacketQueue {

	@Test
	 void testQueueFunction() {
        PacketQueue  myQueue = new PacketQueue(30);
        Queue<Double> queue = new LinkedList<>();

        myQueue.add(2.0);
        queue.offer(2.0);
        myQueue.add(2.1);
        queue.offer(2.1);
        myQueue.add(4.1);
        queue.offer(4.1);
        myQueue.add(5.1);
        queue.offer(5.1);
        myQueue.add(7.1);
        queue.offer(7.1);
        
        
        while (myQueue.size() > 0) {
        	double my = myQueue.poll();
        	double ele = queue.poll();
        	assert(my == ele);
        }
	}

	@Test
	void testQueueMaxSize() {
		PacketQueue  myQueue = new PacketQueue(5);
		assert(myQueue.add(1.0) == true);
		assert(myQueue.add(1.0) == true);
		assert(myQueue.add(1.0) == true);
		assert(myQueue.add(1.0) == true);
		assert(myQueue.add(1.0) == true);
		assert(myQueue.add(1.0) == false);
	}

}
