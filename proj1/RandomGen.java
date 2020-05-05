package proj1;
import java.util.Random;

public class RandomGen {
    public static double NegExpGenerator (double rate) {
        Random r = new Random();
        double u = r.nextDouble();
        return ((-1/rate)* Math.log(1-u));
    }
    
    public static double ParetoGenerator (double rate) {
		double scale = 1;
		double shape = 1;
		return (scale/(Math.pow((1-rate), (1/shape))));
	}

}