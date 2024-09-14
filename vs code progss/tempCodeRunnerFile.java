/*complex no add mul sub cla*/
class Complex
{
float real,img;
Complex()
{
real=0;
img=0;
}
Complex(float a,float b)
{
real=a;
img=b;
}
void Display(Complex c1,Complex c2)
{
System.out.println("first no: ("+c1.real+") + ("c1.img")i)");
System.out.println("second no: ("+c2.real+") + ("c2.img")i)");
}
void sum(Complex c1,Complex c2)
{
System.out.println("sum result: ("c1.real+c2.real") + ("c1.img+c2.img")i)");
}
void sub(Complex c1,Complex c2)
{
System.out.println("sub result: ("c1.real-c2.real") + ("c1.img-c2.img")i)");
}
void mul(Complex c1,Complex c2)
{
System.out.println("sum result: ("c1.real*c2.real-c1.img*c2.img") + ("c1.real*c2.img+c1.img*c2.real")i)");
}
}
class Complex_No
{
public static void main(String args[])
{
Complex cal=new Complex();
float num1,num2;
num1=Float.parseFloat(args[0]);
num=Float.parseFloat(args[1]);
Complex com1=new Complex(num1,num2);
num1=Float.parseFloat(args[2]);
num=Float.parseFloat(args[3]);
Complex com2=new Complex(num1,num2);
cal.Display(com1,com2);
cal.Sum(com1,com2);
cal.Sub(com1,com2);
cal.Mul(com1,com2);
}
}

