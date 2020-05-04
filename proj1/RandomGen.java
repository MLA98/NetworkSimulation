package proj1;
import java.util.Random;

public class RandomGen {
    public static double generator (double rate) {
        Random r = new Random();
        double u = r.nextDouble();
        return ((-1/rate)* Math.log(1-u));
    }
}