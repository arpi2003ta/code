import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

class Producer implements Runnable {
    private final BlockingQueue<Integer> queue;

    public Producer(BlockingQueue<Integer> queue) {
        this.queue = queue;
    }

    @Override
    public void run() {
        int value = 0;
        try {
            while (true) {
                System.out.println("Producer produced: " + value);
                queue.put(value); // Puts item in the queue; waits if queue is full
                value++;
                Thread.sleep(500); // Simulate time taken to produce
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.out.println("Producer interrupted");
        }
    }
}

class Consumer implements Runnable {
    private final BlockingQueue<Integer> queue;

    public Consumer(BlockingQueue<Integer> queue) {
        this.queue = queue;
    }

    @Override
    public void run() {
        try {
            while (true) {
                int value = queue.take(); // Takes item from the queue; waits if queue is empty
                System.out.println("Consumer consumed: " + value);
                Thread.sleep(1000); // Simulate time taken to consume
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.out.println("Consumer interrupted");
        }
    }
}

public class procon {
    public static void main(String[] args) {
        // Shared buffer with a fixed capacity
        BlockingQueue<Integer> queue = new ArrayBlockingQueue<>(5);

        // Create producer and consumer threads
        Thread producerThread = new Thread(new Producer(queue));
        Thread consumerThread = new Thread(new Consumer(queue));

        // Start both threads
        producerThread.start();
        consumerThread.start();
    }
}
