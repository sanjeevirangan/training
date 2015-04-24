using System;


namespace Singleton
{
    class Program
    {
        static void Main()
        {
            //SingletonClass singleton_object = new SingletonClass(); This is not possible with private constructor

            // Calling n times would return the same lunch box
            Console.WriteLine("Lunch box request 1");
            SingletonLunchBox singleton_lunch = SingletonLunchBox.Lunchbox();
            Console.WriteLine("Lunch box request 2");
            SingletonLunchBox singleton_lunch2 = SingletonLunchBox.Lunchbox();
            Console.WriteLine("Lunch box request 3");
            SingletonLunchBox singleton_lunch3 = SingletonLunchBox.Lunchbox();
        }
    }
}
