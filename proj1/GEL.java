package proj1;
import java.util.LinkedList;

public class GEL extends LinkedList<Event>{

    public GEL() {
        super();
    }

    
    // Insert new element in a ascending manner
    public void insert(Event newEvent) {
        for(int i = 0; i < this.size(); i ++) {
            if(newEvent.compareTo(this.get(i)) == -1) {
                this.add(i, newEvent);
                return;
            }
        }

        this.add(newEvent);
    }

}