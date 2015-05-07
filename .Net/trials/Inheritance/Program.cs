using System;


namespace Inheritance_Example_03
{
    class Program
    {
        static void Main()
        {
            AltoK10 objAltoK10 = new AltoK10();
            objAltoK10.Show();
        }

        class car
        {
            public virtual void Show()
            {
                Console.WriteLine("Car Class");
            }
        }
        class Maruti : car
        {
            public new void Show()
            {
                base.Show();
                Console.WriteLine("Maruti Class");
            }
        }
        class Alto : Maruti
        {
            public new void Show()
            {
                base.Show();
                Console.WriteLine("Alto Class");
            }
        }
        class AltoK10 : Alto
        {
            public new void Show()
            {
                base.Show();
                Console.WriteLine("AltoK10 Class");
            }
        }
    }
}
