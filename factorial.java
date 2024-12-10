public class factorial {
    public static int factorial1(int n)
    {
        if(n == 0 || n == 1)
        {
            return 1;
        }
        else
        {
            return n * factorial1( n-1);
        }
    }
    public static void main(String[] args)
    {
        if(args.length == 0)
        {
            System.out.println("please provide a command-line arguments");
            return;
        }
        try
        {
            int num=Integer.parseInt(args[0]);
            if(num<0)
            {
                System.out.println("factorial not possible");
            }
            else
            {
                int result=factorial1(num);
                System.out.println("factorial "+result);
            }
        }
        catch(NumberFormatException e)
        {
            System.out.println("please enter a valid number ");
        }
    }
}
