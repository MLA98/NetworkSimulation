package proj1;
import java.util.Random;
import java.lang.Math; 

public class RandomGen {
	public static double pareto_generator (double rate) {
		double scale = 6820;
		double shape = 4;
		return (scale/(Math.pow((1-rate), (1/shape))));
	}
}

