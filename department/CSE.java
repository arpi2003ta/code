package department;
import java.util.Scanner;
public class CSE 
{
    public String depthead;
    public int studentstrength;
    public String[] subjects;

    public void getdata()
    {
        Scanner scanner=new Scanner(System.in);
        System.out.println("depthead");
        depthead=scanner.nextLine();

        System.out.println("studentstrength");
        studentstrength=scanner.nextInt();
        scanner.nextLine();

        System.out.println("no of subjects");
        int numsubjects=scanner.nextInt();
        scanner.nextLine();

        System.out.println("subjects");
        subjects=new String[numsubjects];
        for(int i=0;i<numsubjects;i++)
        {
            subjects[i]=scanner.nextLine();
        }
        //scanner.close();
    }
    public void showdata()
    {
        System.out.println("depthead"+depthead);
        System.out.println("studentstrength"+studentstrength);
        System.out.println("subjects");
        for(String subject :subjects)
        {
            System.out.println(subject + "");
        }
    }
   
}
