package proj1;
import java.util.LinkedList;

public class PacketQueue extends LinkedList<Double>{
    int maxSize;

    public PacketQueue(int size) {
        // If the queue is supposed to be infinite, 
        // the size should -1.
        super();
        this.maxSize = size;
    }

    @Override
    public boolean add(Double val) {
        if(this.size() == maxSize && maxSize != -1) {
            return false;
        }

        this.addLast(val);
        // Packet added.
        return true;
    }

}