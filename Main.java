import mycomplex.Complex;
import java.util.Scanner;
public class Main
{
    public static void main(String[] args)
    {
        Scanner scanner=new Scanner(System.in);

        System.out.println("enter real 1 complex");
        double real1=scanner.nextDouble();
        System.out.println("enter imag 1 complex");
        double imag1=scanner.nextDouble();

        System.out.println("enter real 2 complex");
        double real2=scanner.nextDouble();
        System.out.println("enter imag 2 complex");
        double imag2=scanner.nextDouble();

        Complex complex1=new Complex(real1,imag1);
        Complex complex2=new Complex(real2,imag2);

        Complex sum=complex1.add(complex2);
        Complex difference=complex1.sub(complex2);
        Complex product=complex1.mul(complex2);

        System.out.println("sum");
        sum.display();

        System.out.println("sub");
        difference.display();

        System.out.println("mul");
        product.display();

        scanner.close();
    }
}