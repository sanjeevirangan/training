using System;


namespace InterfaceAndInheritance
{
    class Program
    {               
        static void Main()
        {
            string bdayMsg = string.Empty;
            Employee objEmployee = new Employee("sanjeevi", "rangan", "sanjeevirangan@gmail.com", new DateTime(1984, 11, 29));
            Console.WriteLine("Enter salary");
            objEmployee.Salary = Convert.ToDecimal(Console.ReadLine());
            Console.WriteLine("Mailing Address");
            objEmployee.MailingAddress = Convert.ToString(Console.ReadLine());
            Console.WriteLine("Enter Due amount to be added.");
            objEmployee.AddToAmountDue(Convert.ToDecimal(Console.ReadLine()));

            Console.WriteLine();
            Console.WriteLine("++++++++++++++++++++++++++++++++++++++++++++++++++");
            Console.WriteLine("Screen name: " + objEmployee.ScreenName());
            Console.WriteLine("Name: " + objEmployee.Full_name);
            Console.WriteLine("DOB: " + objEmployee.dob.ToShortDateString());
            Console.WriteLine("Sun sign: " + objEmployee.SunSign());
            Console.WriteLine("Is Adult: " + objEmployee.isAdult());
            Console.WriteLine("Salary: " + objEmployee.Salary);
            Console.WriteLine("Amount Due: " + objEmployee.RetrieveAmountDue());

            if (objEmployee.isBirthday(out bdayMsg))
            {
                Console.WriteLine(bdayMsg);
            }            
        }
    }

    class Employee : Person, IPayable
    {
        private decimal _salary, _amountDue;
        private string _mailingAddress;
        public Employee(string fn, string ln, string email, DateTime birthDay)
        {
            first_name = fn;
            last_name = ln;
            full_name = first_name + " " + last_name;
            emailid = email;
            dob = birthDay;            
        }

        public decimal Salary
        {
            get { return _salary; }
            set { _salary = value; }
        }
        public string MailingAddress
        {
            get { return _mailingAddress; }
            set { _mailingAddress = value; }
        }
        
        public decimal RetrieveAmountDue()
        {
            return _amountDue;
        }
        public void AddToAmountDue(decimal amt)
        {
            _amountDue += amt;
        }
        public string PaymentAddress()
        {
            return MailingAddress;
        }
    }

    public interface IPayable
    {
        decimal RetrieveAmountDue();
        void AddToAmountDue(decimal amt);
        string PaymentAddress();
    }

    class Person
    {
        public string first_name, last_name, emailid;
        public DateTime dob;
        const int Adult_Age = 18;
        protected string full_name;

        public string Full_name
        {
            get { return full_name; }
            set { full_name = value; }
        }

        public Person()
        {

        }
        public Person(string fn, string ln, string email, DateTime birthDay)
        {
            first_name = fn;
            last_name = ln;
            full_name = first_name + " " + last_name;
            emailid = email;
            dob = birthDay;
        }

        public Person(string fn, string ln, string email)
        {
            first_name = fn;
            last_name = ln;
            emailid = email;
            full_name = first_name + " " + last_name;
        }

        public Person(string fn, string ln, DateTime birthDay)
        {
            first_name = fn;
            last_name = ln;
            dob = birthDay;
            full_name = first_name + " " + last_name;
        }

        public string ScreenName()
        {
            return Full_name.Replace(" ", string.Empty) + dob.Day + dob.Month;
        }

        public bool isAdult()
        {
            if (dob == null)
            {
                Console.WriteLine("Please enter DOB");
                DateTime.TryParse(Console.ReadLine(), out dob);
            }
            return (DateTime.Now.Year - dob.Year) > Adult_Age;
        }

        public bool isBirthday(out string msg)
        {
            if (dob == null)
            {
                Console.WriteLine("Please enter DOB");
                DateTime.TryParse(Console.ReadLine(), out dob);
            }
            bool isBday = false;
            msg = string.Empty;
            if (dob.Month == DateTime.Today.Month && dob.Day == DateTime.Today.Day)
            {

                isBday = true;
                msg = "Happy B'day, " + first_name + " " + last_name + "!!!";
            }
            return isBday;
        }

        public string SunSign()
        {
            return SunSign(dob);
        }

        public string SunSign(DateTime date)
        {
            if (dob == null)
            {
                Console.WriteLine("Please enter DOB");
                DateTime.TryParse(Console.ReadLine(), out dob);
            }
            string sign = string.Empty;
            switch (date.Month)
            {
                case 1:
                    sign = (date.Day <= 20) ? "Capricorn" : "Aquarius";
                    break;
                case 2:
                    sign = (date.Day <= 19) ? "Aquarius" : "Pisces";
                    break;
                case 3:
                    sign = (date.Day <= 20) ? "Pisces" : "Aries";
                    break;
                case 4:
                    sign = (date.Day <= 20) ? "Aries" : "Taurus";
                    break;
                case 5:
                    sign = (date.Day <= 21) ? "Taurus" : "Gemini";
                    break;
                case 6:
                    sign = (date.Day <= 22) ? "Gemini" : "Cancer";
                    break;
                case 7:
                    sign = (date.Day <= 22) ? "Cancer" : "Leo";
                    break;
                case 8:
                    sign = (date.Day <= 23) ? "Leo" : "Virgo";
                    break;
                case 9:
                    sign = (date.Day <= 23) ? "Virgo" : "Libra";
                    break;
                case 10:
                    sign = (date.Day <= 23) ? "Libra" : "Scorpio";
                    break;
                case 11:
                    sign = (date.Day <= 22) ? "Scorpio" : "Sagittarius";
                    break;
                case 12:
                    sign = (date.Day <= 21) ? "Sagittarius" : "Capricorn";
                    break;
            }
            return sign;
        }
    }
}
