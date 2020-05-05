package proj1;
public class Main {    
    public static void main(String[] args) {
    	
        double arrivalRate = Double.parseDouble(args[0]);
        double serviceRate = Double.parseDouble(args[1]);
        int MAXBUFFER = Integer.parseInt(args[2]);
        String distribution = args[3];

        // Initialization
        GEL globalList = new GEL();
        double time = 0;
        PacketQueue buffer = new PacketQueue(MAXBUFFER);
        
        Event firstEvent;
        if(distribution.equals("negExp")) {
        	firstEvent = new Event(time + RandomGen.NegExpGenerator(arrivalRate), RandomGen.NegExpGenerator(serviceRate), EventType.Arrival);
        }
        else {
        	firstEvent = new Event(time + RandomGen.ParetoGenerator(arrivalRate), RandomGen.ParetoGenerator(serviceRate), EventType.Arrival);
        }
        
        globalList.insert(firstEvent);
        
        int dropCount = 0;   
        double busyTime = 0;  
        int length = 0;
        double arrivalCount = 0;
        double queueTotoal = 0;
        int departCount = 0;
        
        double lastQueueChangeTime = 0;
        double queueArea = 0;

        
        // Event Processing
        for (int i = 0; i < 100000; i++){
            
            // get the first event from the GEL;
            Event currEvent = globalList.removeFirst();

            if(currEvent.type == EventType.Arrival){
                arrivalCount += 1;
                queueTotoal += length;
                
                busyTime += currEvent.serviceTime;

                // If the event is an arrival then process-arrival-event;
                time = currEvent.timeStamp;
                
                Event newEvent;
                if(distribution.equals("negExp")) {
                	newEvent = new Event(time + RandomGen.NegExpGenerator(arrivalRate), RandomGen.NegExpGenerator(serviceRate), EventType.Arrival);
                }
                else {
                	newEvent = new Event(time + RandomGen.ParetoGenerator(arrivalRate), RandomGen.ParetoGenerator(serviceRate), EventType.Arrival);
                }
                
                globalList.insert(newEvent);

                if(length == 0) {
                    queueArea += (time - lastQueueChangeTime) * length;
                    lastQueueChangeTime = time;
                    length ++;
                    Event newDepEvent = new Event(time + currEvent.serviceTime, 0, EventType.Departure);
                    globalList.insert(newDepEvent);
                }
                else {
                    if(!buffer.add(currEvent.serviceTime)) {
                        // record drop
                        dropCount ++;
                    }
                    else{
                    	queueArea += (time - lastQueueChangeTime) * length;
                    	lastQueueChangeTime = time;
                        length ++;
                    }
                    // Update statistics which maintain the mean queue-length and the server busy time.
                }
            }
            else {
                departCount ++;
                // Otherwise it must be a departure event and hence process-service-completion
                time = currEvent.timeStamp;

                // Update statistics which maintain the mean queue-length and the server busy time.
                // Since this is a packet departure, we decrement the length.
                queueArea += (time - lastQueueChangeTime) * length;
                lastQueueChangeTime = time;
                length --;

                if(length > 0) {
                    double servT = buffer.poll();
                    Event newDepEvent = new Event(time + servT, servT, EventType.Departure);
                    globalList.insert(newDepEvent);
                }
            }
        }


        // Process output stats
        double utilizationRate = busyTime / time;
        double meanQueueLength = queueArea / time;

        System.out.format("Dropcount: %d\n", dropCount);
        System.out.format("Mean queue Length: %f\n", meanQueueLength);
        System.out.format("Utilization rate: %f\n", utilizationRate);
    }
}