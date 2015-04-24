using System;


namespace BankAccount
{
    class Account
    {
        int account_number;
        string customer_name;
        decimal balance;
        enum AccountType
        {
            savings,
            current,
            loan,
        };
        public enum TransactionType
        {
            deposit,
            withdrawl,
        };
        AccountType account_type;
        public TransactionType transaction_type;

        public Account(int number, string name, char acnt_type_char)
        {
            this.account_number = number;
            this.customer_name = name;
            switch (char.ToLower(acnt_type_char))
            {
                case 's':
                    this.account_type = AccountType.savings;
                    break;
                case 'c':
                    this.account_type = AccountType.current;
                    break;
                case 'l':
                    this.account_type = AccountType.loan;
                    break;
            }
          
        }

        public void DoTransaction(decimal amt)
        {
            switch (this.transaction_type)
            {
                case TransactionType.deposit:
                    Credit(amt);
                    break;
                case TransactionType.withdrawl:
                    Debit(amt);
                    break;
            }
        }

        private void Debit(decimal amt)
        {
            this.balance -= amt;
        }

        private void Credit(decimal amt)
        {
            this.balance += amt; 
        }

        public void ShowAccountSummary()
        {
            Console.WriteLine("Customer Name: " + this.customer_name);
            Console.WriteLine("Account Number: " + this.account_number);
            Console.WriteLine("Account Type: " + this.account_type);
            Console.WriteLine("Balance: " + this.balance);
        }    
    }
}
