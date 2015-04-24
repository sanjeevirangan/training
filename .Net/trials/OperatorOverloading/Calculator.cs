using System;


namespace OperatorOverloading
{
    class Calculator
    {
        int num1, num2;

        public Calculator() { }

        public Calculator(int n1, int n2)
        {
            this.num1 = n1;
            this.num2 = n2;
        }

        public void Display()
        {
            Console.WriteLine(num1 + "," + num2);
        }

        public static Calculator operator +(Calculator cal1, Calculator cal2)
        {
            Calculator result = new Calculator();
            result.num1 = cal1.num1 + cal2.num1;
            result.num2 = cal1.num2 + cal2.num2;
            return result;
        }
    }
}
