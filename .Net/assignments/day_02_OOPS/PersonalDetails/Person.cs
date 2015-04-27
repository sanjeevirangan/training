using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PersonalDetails
{
    class Person
    {
        string first_name, last_name, emailid;
        DateTime dob;
        const int Adult_Age = 18;

        public Person(string fn, string ln, string email, DateTime dob)
        {
            this.first_name = fn;
            this.last_name = ln;
            this.emailid = email;
            this.dob = dob; 
        }

        public Person(string fn, string ln, string email)
        {
            this.first_name = fn;
            this.last_name = ln;
            this.emailid = email;
        }

        public Person(string fn, string ln, DateTime dob)
        {
            this.first_name = fn;
            this.last_name = ln;
            this.dob = dob; 
        }

        public bool isAdult()
        {
            DateTime today = DateTime.Now;
            int age =  today.Year - this.dob.Year;
            if (age == Adult_Age && this.dob.Month >= today.Month)
            {
                age += 1;
            }
            return age > Adult_Age; 
        }

        public bool isBirthday()
        {
            bool isBday = false;
            if (this.dob.Month == DateTime.Now.Month && this.dob.Date == DateTime.Now.Date)
            {
                isBday = true;
                Console.WriteLine("Happy B'day, " + first_name + " " + last_name); 
            }
            return isBday;
        }

        public string GetSunSign()
        {
            return "";
 
        }
    }
}
