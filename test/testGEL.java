package test;

import static org.junit.jupiter.api.Assertions.*;
import java.util.Random;
import proj1.Event;


import org.junit.jupiter.api.Test;

import proj1.GEL;

class testGEL {

	@Test
	void test() {
		GEL list = new GEL();
		for(int i = 0; i < 1000; i ++) {
			Random rand = new Random();
			double u = rand.nextDouble();
			Event e = new Event(u, 0.0, null);
			list.insert(e);
		}
		
		double lastVal = -1.0;
		for(Event e : list) {
			System.out.print(e.getTimeStamp());
			assert(lastVal < e.getTimeStamp());
			lastVal = e.getTimeStamp();
		}
	}

}
