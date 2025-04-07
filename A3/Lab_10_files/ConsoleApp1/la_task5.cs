using System;

namespace BasicMathApp
{
    class Calculator
    {
        static void Main(string[] args)
        {
            try
            {
                // Accepting user input
                Console.Write("Enter first number: ");
                double num1 = Convert.ToDouble(Console.ReadLine());

                Console.Write("Enter second number: ");
                double num2 = Convert.ToDouble(Console.ReadLine());

                // Performing operations
                double sum = num1 + num2;
                double diff = num1 - num2;
                double product = num1 * num2;
                double quotient = num2 != 0 ? num1 / num2 : double.NaN;

                // Checking if sum is even or odd
                if (sum % 2 == 0)
                    Console.WriteLine("The sum is even.");
                else
                    Console.WriteLine("The sum is odd.");

                // Displaying results
                Console.WriteLine("Addition: " + sum);
                Console.WriteLine("Subtraction: " + diff);
                Console.WriteLine("Multiplication: " + product);
                Console.WriteLine("Division: " + (double.IsNaN(quotient) ? "Undefined (division by zero)" : quotient.ToString()));
            }
            catch (FormatException)
            {
                Console.WriteLine("Error: Please enter valid numeric values.");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Unexpected error: " + ex.Message);
            }
        }
    }
}
