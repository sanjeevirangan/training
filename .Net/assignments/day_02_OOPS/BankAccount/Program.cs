using System;

namespace BankAccount
{
    class Program
    {
        static void Main()
        {
            int account_number;
            decimal amount;
            char tran_type_char, accnt_type_char;
            
            Console.WriteLine("Enter Account number");
            if (!int.TryParse(Console.ReadLine(), out account_number))
            {
                Console.WriteLine("Please enter a valid account number");
                return;
            }

            Console.WriteLine("Enter customer name");
            string customer_name = Console.ReadLine();
            if (customer_name == string.Empty || string.IsNullOrWhiteSpace(customer_name))
            {
                Console.WriteLine("Please enter a valid customer name");
                return;
            }

            Console.WriteLine("Enter account type. \n'S' for savings." +
                                "\n'L' for loan." +
                                "\n'C' for current.");

            if (!char.TryParse(Console.ReadLine(), out accnt_type_char) && (char.ToLower(accnt_type_char) != 'l' ||
                                char.ToLower(accnt_type_char) != 's' || char.ToLower(accnt_type_char) != 'c'))
            {
                Console.WriteLine("Please enter a valid transaction type");
                return;
            }

            Account account = new Account(account_number, customer_name, accnt_type_char);

           
            Console.WriteLine("Enter transaction type. \n'D' for Deposit. \n'W' for withdrawl.");
            if (!char.TryParse(Console.ReadLine(), out tran_type_char) && (char.ToLower(tran_type_char) != 'w' || char.ToLower(tran_type_char) != 'd'))
            {
                Console.WriteLine("Please enter a valid transaction type");
                return;
            }
            else 
            {
                if (char.ToLower(tran_type_char) == 'w')
                {
                    account.transaction_type = Account.TransactionType.withdrawl;
                }
                else if (char.ToLower(tran_type_char) == 'd')
                {
                    account.transaction_type = Account.TransactionType.deposit;
                }
            }  
          
            Console.WriteLine("Enter Amount");
            if (!decimal.TryParse(Console.ReadLine(), out amount))
            {
                Console.WriteLine("Please enter a valid amounts");
                return;
            }
            
            account.DoTransaction(amount);
            account.ShowAccountSummary();
        }
    }
}
