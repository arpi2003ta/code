import java.util.Scanner;
public class timeaddition 
{
    public static void main(String[] args)
    {
        Scanner scanner=new Scanner(System.in);

        System.out.println("enter the 1 time");
        System.out.println("Hours");
        int hours1=scanner.nextInt();
        System.out.println("minutes");
        int minutes1=scanner.nextInt();
        System.out.println("secondss");
        int seconds1=scanner.nextInt();

        System.out.println("enter the 2 time");
        System.out.println("Hours");
        int hours2=scanner.nextInt();
        System.out.println("minutes");
        int minutes2=scanner.nextInt();
        System.out.println("secondss");
        int seconds2=scanner.nextInt();

        int totalseconds=seconds1 + seconds2;
        int carryminutes=totalseconds/60;
        totalseconds=totalseconds%60;

        int totalminutes=minutes1 + minutes2+carryminutes;
        int carryhours=totalminutes/60;
        totalminutes=totalminutes%60;

        int totalhours=hours1 + hours2 + carryhours;

        System.out.println("total time   "+totalhours+":"+totalminutes+":"+totalseconds);
        scanner.close();

    }
    
}
