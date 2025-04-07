//using System;

//namespace StudentApp
//{
//    class Student
//    {
//        // Properties
//        public string Name { get; set; }
//        public int ID { get; set; }
//        public float Marks { get; set; }

//        // Default constructor
//        public Student()
//        {
//            Name = "Unknown";
//            ID = 0;
//            Marks = 0;
//        }

//        // Parameterized constructor
//        public Student(string name, int id, float marks)
//        {
//            Name = name;
//            ID = id;
//            Marks = marks;
//        }

//        // Copy constructor
//        public Student(Student other)
//        {
//            Name = other.Name;
//            ID = other.ID;
//            Marks = other.Marks;
//        }

//        // Method to get grade
//        public string GetGrade()
//        {
//            if (Marks >= 90) return "A";
//            else if (Marks >= 75) return "B";
//            else if (Marks >= 60) return "C";
//            else return "D";
//        }

//        // Wrapper method
//        public static void Run()
//        {
//            Student s1 = new Student("Alice", 101, 88.5f);
//            Console.WriteLine("Student Details:");
//            Console.WriteLine($"Name: {s1.Name}, ID: {s1.ID}, Marks: {s1.Marks}, Grade: {s1.GetGrade()}");

//            // Copy constructor example
//            Student s2 = new Student(s1);
//            Console.WriteLine("\nCopied Student:");
//            Console.WriteLine($"Name: {s2.Name}, ID: {s2.ID}, Marks: {s2.Marks}, Grade: {s2.GetGrade()}");
//        }
//    }

//    class StudentIITGN : Student
//    {
//        public string Hostel_Name_IITGN { get; set; }

//        public StudentIITGN(string name, int id, float marks, string hostel) : base(name, id, marks)
//        {
//            Hostel_Name_IITGN = hostel;
//        }

//        // Wrapper method
//        public static void Run()
//        {
//            StudentIITGN s3 = new StudentIITGN("Bob", 202, 92.0f, "A-Block");
//            Console.WriteLine("\nIITGN Student Details:");
//            Console.WriteLine($"Name: {s3.Name}, ID: {s3.ID}, Marks: {s3.Marks}, Grade: {s3.GetGrade()}, Hostel: {s3.Hostel_Name_IITGN}");
//        }
//    }

//    class Program
//    {
//        // Single entry point
//        static void Main(string[] args)
//        {
//            Student.Run();
//            StudentIITGN.Run();
//        }
//    }
//}
