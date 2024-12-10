public class Example {
    static int counter;

    static {
        counter = 10; // Initialize static variable
        System.out.println("Static block executed");
    }

    public static void main(String[] args) {
        System.out.println("Counter: " + counter);
    }
}
