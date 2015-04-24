using System;

namespace Singleton
{
    class SingletonLunchBox
    {
        // Return the same lunch box instance for all the calls
        private SingletonLunchBox()
        {
            // Pack the box
            Console.WriteLine("Packing singleton Lunch box");
            Console.WriteLine("Adding bisibela baath");
            Console.WriteLine("Lunch box ready");
        }

        private static SingletonLunchBox _lucnhbox;

        public static SingletonLunchBox Lunchbox()
        {
            // If there was no istance, create one or return the exisiting.
            if (_lucnhbox == null)
            {
                _lucnhbox = new SingletonLunchBox();
            }
            Console.WriteLine("Returning lunch box\n");
            return _lucnhbox;          
        }
    }
}
