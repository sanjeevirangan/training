using System;


namespace ATM_Events
{
    class Program
    {
        static void Main(string[] args)
        {
            Accounts acnt = new Accounts();
            acnt.OnMessageCalled += new Accounts.Message(acnt.PrintMessage);
            Console.WriteLine("Enter pin number");
            int pin_num = int.Parse(Console.ReadLine());
            acnt.Authenticate(pin_num);
        }
    }
}
