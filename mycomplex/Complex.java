package mycomplex;
//import java.util.Scanner;
public class Complex 
{
    private double real;
    private double imag;

    public Complex(double real,double imag)
    {
        this.real=real;
        this.imag=imag;
    }

    public Complex add(Complex other)
    {
        double realsum= this.real + other.real;
        double imagsum= this.imag + other.imag;
        return new Complex(realsum , imagsum);
    }

    public Complex sub(Complex other)
    {
        double realsub= this.real - other.real;
        double imagsub= this.imag - other.imag;
        return new Complex(realsub , imagsub);
    }

    public Complex mul(Complex other)
    {
        double realmul= this.real * other.real - this.imag * other.imag;
        double imagmul= this.real * other.imag + this.imag * other.real;
        return new Complex(realmul , imagmul);
    }

    public void display()
    {
        if(imag >= 0)
        {
            System.out.println(real + "+"+imag +"i");
        }
        else
        {
            System.out.println(real + "-"+Math.abs(imag) +"i");

        }
    }
}

