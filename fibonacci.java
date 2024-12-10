public class fibonacci 
{
    public static void main (String[] args)
    {
        if(args.length != 1)
        {
            System.out.println("please enter a string integer as a command line arguments");
            return;
        }

        int n;
        try
        {
            n=Integer.parseInt(args[0]);
        }
        catch(NumberFormatException e)
        {
            System.out.println("please enter a valid integer ");
            return;
        }

        if(n <= 0)
        {
            System.out.println("please enter a positive  integer ");
            return;
        }

        int first=0,second=1;
        System.out.println("fibonacci series ");
        for(int i=1;i<=n;i++)
        {
            System.out.println(first +"");
            int next=first +second;
            first = second;
            second = next;
        }

    }
}
