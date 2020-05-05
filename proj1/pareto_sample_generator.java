package proj1;
import java.util.Random;
import java.lang.Math; 

public class RandomGen {
	public static double pareto_generator (double rate) {
		double scale = 1;
		double shape = 1;
		return (scale/(Math.pow((1-rate), (1/shape))));
	}
}

