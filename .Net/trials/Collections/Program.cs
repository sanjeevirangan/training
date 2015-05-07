using System;
using System.Collections.Generic;


namespace Collections
{
    class Program
    {
        static void Main()
        {
            System.Collections.ArrayList al = new System.Collections.ArrayList();
            al.Add("Sanjeevi");
            al.Add(2);
            al.Add(4.0);
            al.Add(DateTime.Now);
            foreach (object item in al)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine("+++++++++++++++++++++++++++++++++++++++++");
            al.Insert(1, "Rangan");
            al.Insert(2, "Rocks!!!");
            foreach (object item in al)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine("+++++++++++++++++++++++++++++++++++++++++\n");
            al.RemoveAt(5);
            
            al.Remove("Rocks!!!");
            System.Collections.IEnumerator ie = al.GetEnumerator();
            while(ie.MoveNext())
            {
                Console.WriteLine(ie.Current);
            }             
            Console.WriteLine("+++++++++++++++++++++++++++++++++++++++++\n");
            Console.WriteLine("Size: " + al.Count);

            System.Collections.Hashtable ht = new System.Collections.Hashtable();
            ht.Add("IN", "INDIA");
            ht.Add("UK", "UNITED KINGDOM");
            ht.Add("US", "UNITED STATES OF AMERICA");

            foreach (string key in ht.Keys)
            {
                Console.WriteLine(ht[key]);
            }

            List<Employee> emp = new List<Employee>();
            emp.Add(new Employee(001, "sanjeevi", "IT", 100000000000));
            emp.Add(new Employee(002, "somebody", "IT", 10000000000));
            emp.Add(new Employee(003, "nobody", "IT", 1000000000));
            emp.Add(new Employee(004, "whatever", "IT", 100000000));
            emp.Add(new Employee(005, "genius", "IT", 10000000));
            double total_salary = 0;
            foreach (Employee item in emp)
            {
                Console.WriteLine(item.EmpId + "," + item.Name + "," + item.Dept + "," + item.Salary);
                total_salary += item.Salary;
            }
            Console.WriteLine("Total Salary: " + total_salary);
            Console.WriteLine("+++++++++++++++++++++++++++++++++++++++++\n");

            Dictionary<string, CountryInfo> country_dict = new Dictionary<string, CountryInfo>();
            country_dict.Add("IN", new CountryInfo("INDIA", "New Delhi", "Rupee"));
            country_dict.Add("NP", new CountryInfo("NEPAL", "KATHMANDU", "Nepaleese Rupee"));
            foreach (KeyValuePair<string, CountryInfo> kv in country_dict)
            {
                Console.WriteLine(kv.Key + ": " + kv.Value.CountryName + "," + kv.Value.Capital + "," + kv.Value.Currency);
            }
            Console.WriteLine("+++++++++++++++++++++++++++++++++++++++++\n");
        }
    }

    class CountryInfo
    {
        string countryName;
        public string CountryName
        {
          get { return countryName; }
          set { countryName = value; }
        }
        string capital;
        public string Capital
        {
            get { return capital; }
            set { capital = value; }
        }
        string currency;
        public string Currency
        {
            get { return currency; }
            set { currency = value; }
        }

        public CountryInfo(string countryName, string capital, string currency)
        {
            this.CountryName = countryName;
            this.Capital = capital;
            this.Currency = currency;
        }
    }

    class Employee
    {
        int empId;

        public int EmpId
        {
            get { return empId; }
            set { empId = value; }
        }
        string name;

        public string Name
        {
            get { return name; }
            set { name = value; }
        }

        string dept;

        public string Dept
        {
            get { return dept; }
            set { dept = value; }
        }

        double salary;

        public double Salary
        {
            get { return salary; }
            set { salary = value; }
        }

        public Employee(int empId, string name, string dept, double salary)
        {
            this.EmpId = empId;
            this.Name = name;
            this.Dept = dept;
            this.Salary = salary;
        }
    }
}
