using System;


namespace CalculatorDelegate
{
    class Program
    {
        // Declare delegate
        public delegate void MyCalc(int x, int y);
        static void Main(string[] args)
        {
            Addition add = new Addition();
            Subtraction sub = new Subtraction();
            Multiply mul = new Multiply();
            Divide div = new Divide();

            // legcay style: before 2.0
            MyCalc c = new MyCalc(add.Add);

            // modern style: Delegate inference
            MyCalc c1 = add.Add;
            c1 += sub.Sub;
            c1 += mul.Mul;
            c1 += div.Div;
            c1(100, 200);
        }
    }
}
