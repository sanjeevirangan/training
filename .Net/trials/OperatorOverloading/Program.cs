using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OperatorOverloading
{
    class Program
    {
        static void Main(string[] args)
        {
            Calculator add1 = new Calculator(10, 20);
            Calculator add2 = new Calculator(30, 40);
            Calculator result = add1 + add2;
            result.Display();
        }
    }
}
