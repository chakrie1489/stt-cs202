//using System;

//namespace LoopAndFunctionApp
//{
//    class LoopTasks
//    {
//        // Function to calculate factorial
//        static long Factorial(int n)
//        {
//            long result = 1;
//            for (int i = 1; i <= n; i++)
//            {
//                result *= i;
//            }
//            return result;
//        }

//        static void Main(string[] args)
//        {
//            // For loop to print numbers from 1 to 10
//            Console.WriteLine("Numbers from 1 to 10:");
//            for (int i = 1; i <= 10; i++)
//            {
//                Console.Write(i + " ");
//            }
//            Console.WriteLine();  // new line

//            // While loop to take user input
//            string input = "";
//            while (input.ToLower() != "exit")
//            {
//                Console.Write("\nEnter a number to find factorial or type 'exit' to quit: ");
//                input = Console.ReadLine();

//                if (input.ToLower() != "exit")
//                {
//                    if (int.TryParse(input, out int num) && num >= 0)
//                    {
//                        long fact = Factorial(num);
//                        Console.WriteLine("Factorial of " + num + " is: " + fact);
//                    }
//                    else
//                    {
//                        Console.WriteLine("Please enter a valid non-negative integer.");
//                    }
//                }
//            }

//            Console.WriteLine("Program ended.");
//        }
//    }
//}
