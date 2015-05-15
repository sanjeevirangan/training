using System;


namespace ATM_Events
{
    class Accounts
    {
        int acnt_id;
        string name;
        public double balance;

        public void PrintMessage(string msg)
        {
            Console.WriteLine(msg);
        }

        public delegate void Message(string msg); // delegate
        public event Message OnMessageCalled;   // event

        public void Authenticate(int pin)
        {
            if (pin == 1234)
            {
                ShowMenu();
            }
            else
            {
                //PrintMessage("Invalid pin entered!");
                OnMessageCalled("Invalid pin enetered!");
            }
        }

        private void ShowMenu()
        {            
            while (true)
            {
                Console.WriteLine("Select transaction");
                Console.WriteLine("1. Deposit\n" +
                                  "2. Withdraw\n" +
                                  "3. Balance\n");

                int user_input = int.Parse(Console.ReadLine());
                switch (user_input)
                {
                    case 1: Deposit();
                        break;
                    case 2: Withdraw();
                        break;
                    case 3: ShowBal();
                        break;
                    default: Console.WriteLine("Invalid option\n");
                        Environment.Exit(0);
                        break;
                }
            }
        }

        private void Deposit()
        {
            int deposit;
            Console.WriteLine("Enter deposit amt");
            int.TryParse(Console.ReadLine(), out deposit);

            if (deposit <= 0)
            {
                //PrintMessage("Cannot deposit amount less than 1\n");
                OnMessageCalled("Cannot deposit amount less than 1");
            }
            else
                balance += deposit;
        }
        private void Withdraw()
        {
            int withdraw;
            Console.WriteLine("Enter withdrwal amt");
            int.TryParse(Console.ReadLine(), out withdraw);
            if (withdraw > balance)
            {
               //rintMessage("Insufficent balance\n");
                OnMessageCalled("Insufficent balance");
            }
            else
            {
                balance -= withdraw;
            }
        }
        private void ShowBal()
        {
            Console.WriteLine("Balance as of " + DateTime.Now.ToLongTimeString() + ": " + balance);
        }

        public Accounts()
        {
            acnt_id = 1234;
            balance = 500;
            name = "sanjevei";
        }            
    }
}
