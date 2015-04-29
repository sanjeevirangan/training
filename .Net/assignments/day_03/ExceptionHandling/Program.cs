using System;


namespace ExceptionHandling
{
    class Program
    {
        static void Main()
        {
            int n1, n2;
            Console.WriteLine("Enter value 1");
            int.TryParse(Console.ReadLine(), out n1);
            Console.WriteLine("Enter value 2");
            int.TryParse(Console.ReadLine(), out n2);
            UserTrail objUserTrail = new UserTrail(n1, n2);
            try
            {
                objUserTrail.show();
                objUserTrail.calculate();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                Console.WriteLine("=============================================");
                Main();
            }


            try
            {
                Console.WriteLine("Enter a string to test.");
                objUserTrail.TestString(Console.ReadLine());
            }
            catch (NoMatchException ex)
            {
                Console.WriteLine(ex.Message);
            }
        }

        class UserTrail
        {
            protected int val1, val2;

            public UserTrail(int n1, int n2)
            {
                val1 = n1;
                val2 = n2;
            }

            public void show()
            {
                string msg1 = "Val1 is not less than zero";
                string msg2 = "Val2 is not less than zero";
                if (val1 < 0)
                {
                    msg1 = "Val1 is less than zero: " + val1.ToString();
                }
                if (val2 < 0)
                {
                    msg2 = "Val2 is less than zero: " + val2.ToString(); 
                }
                Console.WriteLine(msg1);
                Console.WriteLine(msg2);
            }
            public void calculate()
            {
                if (val1 < 0 || val2 <0)
                {
                    throw new Exception("Negative number found");
                }
                Console.WriteLine("Difference: " + (val1 - val2).ToString());
            }

            public void TestString(string str)
            {
                if (string.Compare(str, "ITC Infotech") != 0)
                {
                    throw new NoMatchException(str);
                }
                else
                {
                    Console.WriteLine(str);
                }
            }
        }

        class NoMatchException : Exception
        {
            protected string _str = string.Empty;
            public NoMatchException() { }
            public NoMatchException(string str)
            {
                _str = str;                
            }

            public override string Message
            {
                get
                {
                    string msg = "A non mathcing string found";
                    if (!string.IsNullOrEmpty(_str))
                    {
                        msg += ": " + _str;
                    }
                    return msg;
                }
            }            
        }
    }
}
