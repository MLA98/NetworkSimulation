package proj1;

enum EventType
{ 
    Arrival, Departure; 
} 

public class Event implements Comparable<Event>{
    double timeStamp; 
    double serviceTime;
    EventType type;

    public Event(double timeStamp, double serviceTime, EventType type) {
        this.timeStamp = timeStamp;
        this.serviceTime = serviceTime;
        this.type = type;
    }

    @ Override
    public int compareTo(Event anotherEvent) {
        if (this.timeStamp == anotherEvent.timeStamp) {
            return 0;
        }
        
        return this.timeStamp < anotherEvent.timeStamp ? -1 : 1;
    }    
    
    public double getTimeStamp() {
    	return timeStamp;
    }
    
    public double getServiceTime() {
    	return serviceTime;
    }
}