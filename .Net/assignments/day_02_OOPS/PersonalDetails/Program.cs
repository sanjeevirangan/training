using System;


namespace PersonalDetails
{
    class Program
    {
        static void Main()
        {
            string bdayMsg = string.Empty;
            Person objPerson = new Person("Sanjeevi", "Rangan", "sanjeevirangan@gmail.com", new DateTime(1984, 04, 27));
            
            Console.WriteLine("Name: " + objPerson.Full_name);
            Console.WriteLine("DOB: " + objPerson.dob.ToShortDateString());
            Console.WriteLine("Sun sign: " + objPerson.SunSign());
            Console.WriteLine("Is Adult: " + objPerson.isAdult());

            if (objPerson.isBirthday(out bdayMsg))
            {
                Console.WriteLine(bdayMsg);
            }
        }
    }
}
