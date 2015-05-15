using System;


namespace MobileDelegate
{
    class Airtel
    {
        int[] numbers = { 98453, 98454, 98456, 98457, 98458 };
        public void Message(string msg)
        {
            foreach (int m in numbers)
            {
                Console.WriteLine("Airtel: " + m + "," + msg);
            }
        }
    }
    class Vodafone
    {
        int[] numbers = { 8453, 8454, 8456, 8457, 8458 };
        public void Message(string msg)
        {
            foreach (int m in numbers)
            {
                Console.WriteLine("Vodafone: " + m + "," + msg);
            }
        }
    }
    class Idea
    {
        int[] numbers = { 97453, 97454, 97456, 97457, 97458 };
        public void Message(string msg)
        {
            foreach (int m in numbers)
            {
                Console.WriteLine("Idea: " + m + "," + msg);
            }
        }
    }
    class Docomo
    {
        int[] numbers = { 99453, 99454, 99456, 99457, 99458 };
        public void Message(string msg)
        {
            foreach (int m in numbers)
            {
                Console.WriteLine("Docomo: " +  m + "," + msg);
            }
        }
    }
}
