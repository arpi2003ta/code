import java.util.Scanner;
public class lcm
{
    public static int gcd(int a,int b)
    {
            while(b!= 0)
            {
                int temp =b;
                b=a%b;
                a=temp;
            }
            return a;
    }
    public static int lcm1(int a,int b)
    {
        return (a*b)/gcd(a,b);
    }
    public static void main(String[] args)
    {
        Scanner scanner=new Scanner(System.in);
        System.out.println("enter first no");
        int num1=scanner.nextInt();
        System.out.println("enter first no");
        int num2=scanner.nextInt();
        int result=lcm1(num1,num2);
        System.out.println("result"+result);
        scanner.close();
    }
}