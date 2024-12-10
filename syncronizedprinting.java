class Student
{
    public synchronized void print(String word)
    {
        System.out.print("["+word+"]");
    }
}

public class syncronizedprinting 
{
    public static void main(String[] args)
    {
        Student student = new Student();

        Thread t1 = new Thread(() -> student.print("All"));
        Thread t2 = new Thread(() -> student.print("the"));
        Thread t3 = new Thread(() -> student.print("best"));

        try
        {
            t1.start();
            t1.join();
            t2.start();
            t2.join();
            t3.start();
            t3.join();
        }
        catch(InterruptedException e)
        {
            e.printStackTrace();
            
        }
    }
}
