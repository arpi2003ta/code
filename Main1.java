import department.CSE;
import department.IT;

public class Main1 
{
    public static void main(String[] args)
    {
        CSE cse=new CSE();
        IT it=new IT();

        System.out.println("CSE detsils");
        cse.getdata();

        System.out.println("IT detsils");
        it.getdata();

        System.out.println("CSE detsils");
        cse.showdata();

        System.out.println("IT detsils");
        it.showdata();
    }
}
