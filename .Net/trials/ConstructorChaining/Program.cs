using System;



namespace ProjectInfo
{
    class Program
    {
        static void Main(string[] args)
        {          
            Child child = new Child("hi");
        }
    }

    class Parent
    {
        public Parent()
        {
            Console.WriteLine("Parent Class constructor");
        }
        public Parent(string msg)
        {
            Console.WriteLine("Parent Class Parameterized constructor: " + msg);
 
        }
    }
    class Child : Parent
    {
        public Child()
        {
            Console.WriteLine("Child class constructor");
        }
        public Child(string msg):base("from child")
        {
            Console.WriteLine("Child class parameterized constructor: " + msg );
        }
    }
}
