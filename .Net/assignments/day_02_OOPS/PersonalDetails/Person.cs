using System;

namespace PersonalDetails
{
    class Person
    {
        public string first_name, last_name, emailid;
        public DateTime dob;
        const int Adult_Age = 18;
        private string full_name;

        public string Full_name
        {
            get { return full_name; }
            set { full_name = value; }
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
                    sign = (date.Day <= 20) ?  "Capricorn" : "Aquarius";
                    break;
                case 2: 
                    sign = (date.Day <= 19) ? "Aquarius" : "Pisces";
                    break;
                case 3:
                    sign =  (date.Day <= 20) ? "Pisces" : "Aries";
                    break;
                case 4: 
                    sign = (date.Day <= 20) ? "Aries" : "Taurus";
                    break;
                case 5:
                    sign = (date.Day <= 21) ? "Taurus" : "Gemini";
                    break;
                case 6: 
                    sign =  (date.Day <= 22) ? "Gemini" : "Cancer";
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
