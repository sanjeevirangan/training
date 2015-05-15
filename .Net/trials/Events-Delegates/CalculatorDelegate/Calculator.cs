using System;


namespace CalculatorDelegate
{    
    class Addition
    {
        public void Add(int x, int y)
        {
            Console.WriteLine("Addition: " + (x + y));
        }
    }

    class Subtraction
    {
        public void Sub(int x, int y)
        {
            Console.WriteLine("subtraction: " + (x - y));
        }
    }

    class Multiply
    {
        public void Mul(int x, int y)
        {
            Console.WriteLine("Multiply: " + (x * y));
        }
    }

    class Divide
    {
        public void Div(int x, int y)
        {
            Console.WriteLine("Divide: " + (x / y));
        }
    }
}
