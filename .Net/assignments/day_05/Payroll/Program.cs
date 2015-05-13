using System;
using System.Collections.Generic;


namespace Payroll
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("******************************************************************");
            Console.WriteLine("******************Welcome to HSB Payroll**************************");
            Console.WriteLine("******************************************************************");
            Console.WriteLine("Please enter employee type:\n1. Full time employee.\n2. Part time employee.");
            try
            {
                int choice = int.Parse(Console.ReadLine());
                switch (choice)
                {
                    case 1:
                        Console.WriteLine("Enter first name, last name, employeed id, manager");
                        FullTimeEmployee FTE = new FullTimeEmployee(Console.ReadLine(),
                                                                    Console.ReadLine(),
                                                                    int.Parse(Console.ReadLine()),
                                                                    Console.ReadLine());
                        Console.WriteLine("Enter apprisal rating.");
                        FTE.Apprisal_rating = int.Parse(Console.ReadLine());
                        FTE.Compute_Salary();
                        FTE.ShowDetails();
                        break;
                    case 2:
                        Console.WriteLine("Enter first name, last name, employeed id, manager");
                        PartTimeEmployee PTE = new PartTimeEmployee(Console.ReadLine(),
                                                                    Console.ReadLine(),
                                                                    int.Parse(Console.ReadLine()),
                                                                    Console.ReadLine());
                        Console.WriteLine("Enter hourly rate of pay percentage.");
                        PTE.Pay_rate = double.Parse(Console.ReadLine());
                        Console.WriteLine("Enter shift start time in 24 hrs format. EX: '9:30'.");
                        PTE.Shift_start_time = TimeSpan.Parse(Console.ReadLine());
                        Console.WriteLine("Enter shift end time in 24 hrs format. EX: '17:30'.");
                        PTE.Shift_end_time = TimeSpan.Parse(Console.ReadLine());
                        Console.WriteLine("Enter number of days worked in current week.");
                        PTE.Days_worked = int.Parse(Console.ReadLine());
                        PTE.Compute_Salary();
                        PTE.ShowDetails();
                        break;
                    default:
                        Console.WriteLine("Invalid option.");
                        break;
                }
            }
            catch (FormatException ex)
            {
                Console.WriteLine("Invalid data!\n" + ex.Message);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            finally
            {
                Console.WriteLine("******************************************************************");
                Console.WriteLine("*******************Quitting HSB Payroll***************************");
                Console.WriteLine("******************************************************************");
            }  
        }
    }

    abstract class Employee
    {
        protected string first_name;
        protected string last_name;
        protected int employee_id;
        protected string manager;
        protected double gross_salary;
        public string Full_name
        {
            get { return first_name + " " + last_name; }
        }

        public Employee(string first_name, string last_name, int employee_id, string manager)
        {
            this.first_name = first_name;
            this.last_name = last_name;
            this.employee_id = employee_id;
            this.manager = manager;            
        }
        public abstract double Compute_Salary();
        public virtual void ShowDetails()
        {
            Console.WriteLine("First name: " + first_name);
            Console.WriteLine("Last name: " + last_name);
            Console.WriteLine("Full name: " + Full_name);
            Console.WriteLine("Employee ID: " + employee_id);
            Console.WriteLine("Gross salary: " + gross_salary);
        }
    }

    class FullTimeEmployee : Employee
    {
        // private members
        const int Basic = 7500;
        int apprisal_rating;

        // public memebers        
        public int Apprisal_rating
        {
            get { return apprisal_rating; }
            set { apprisal_rating = value; }
        }
        public double Variable_rate
        {
            get
            {
                if (apprisal_rating <= 2)
                {
                    return 0;
                }
                else if (apprisal_rating <= 5)
                {
                    return 0.05;
                }
                else if (apprisal_rating <= 7)
                {
                    return 0.07;
                }
                else if (apprisal_rating <= 9)
                {
                    return 0.09;
                }
                else
                {
                    return 1;
                }
            }
        }
        public double Vairable_pay
        {
            get { return Basic * Variable_rate; }
        }

        public FullTimeEmployee(string first_name, string last_name, int employee_id, string manager) : 
            base(first_name, last_name, employee_id, manager) { }
        
        // Public methods
        public override double Compute_Salary()
        {
            gross_salary = Vairable_pay + Basic;
            return gross_salary;
        }
        public override void ShowDetails()
        {
            Console.WriteLine("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
            Console.WriteLine("+++++++++++++++++++++++Employee Details+++++++++++++++++++++++++++");
            Console.WriteLine("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
            base.ShowDetails();
            Console.WriteLine("Quaterly apprisal rating " + apprisal_rating);
            Console.WriteLine("Variable rate: " + Variable_rate);
            Console.WriteLine("Variable pay: " + Vairable_pay);
            Console.WriteLine("Basic pay: " + Basic);
            Console.WriteLine("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
        }
    }

    class PartTimeEmployee : Employee
    {
        const int Base_Pay = 7500;
        double pay_rate;
        int days_worked;
        TimeSpan shift_start_time, shift_end_time;
        
        public TimeSpan Shift_end_time
        {
            get { return shift_end_time; }
            set { shift_end_time = value; }
        }
        public TimeSpan Shift_start_time
        {
            get { return shift_start_time; }
            set { shift_start_time = value; }
        }
        public int Days_worked
        {
            get { return days_worked; }
            set { days_worked = value; }
        }
        public double Pay_rate
        {
            get { return pay_rate; }
            set { pay_rate = value; }
        }
        public double Hourly_pay
        {
            get { return ((pay_rate * Base_Pay / 100)/30)/24; }
        }
        public double Hours_worked
        {
            get { return Compute_Hours_Worked(days_worked, Shift_start_time, Shift_end_time); }
        }        

        public PartTimeEmployee(string first_name, string last_name, int employee_id, string manager) : 
            base(first_name, last_name, employee_id, manager) { }

        private double Compute_Hours_Worked(int num_days, TimeSpan start_time, TimeSpan end_time)
        {
            TimeSpan shift_time = end_time.Subtract(start_time);
            if (shift_time.TotalHours < 0)
            {
                throw new Exception("Invalid Shift timings.");
            }
            return shift_time.TotalHours * num_days;            
        }

        public override double Compute_Salary()
        {            
            gross_salary =  Hours_worked * Hourly_pay;
            return gross_salary;
        }

        public override void ShowDetails()
        {
            Console.WriteLine("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
            Console.WriteLine("+++++++++++++++++++++++Employee Details+++++++++++++++++++++++++++");
            Console.WriteLine("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
            base.ShowDetails();
            Console.WriteLine("Shift timing: " + Shift_start_time + " to " + Shift_end_time);
            Console.WriteLine("Total hours worked: " + Hours_worked);
            Console.WriteLine("Wages per hour: " + Hourly_pay);
            Console.WriteLine("Days worked: " + Days_worked);            
            Console.WriteLine("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
        }
    }
}
