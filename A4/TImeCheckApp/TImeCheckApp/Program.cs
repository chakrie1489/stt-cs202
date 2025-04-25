using System;
using System.Threading;
using System.Timers;
using Timer = System.Timers.Timer;

namespace TimeCheckApp
{
    // Publisher class
    public class AlarmClock
    {
        // Define the event using EventHandler
        public event EventHandler? RaiseAlarm;

        // Method to check the time and raise the event
        public void CheckTime(string userTime, ManualResetEvent alarmTriggered)
        {
            Timer timer = new Timer(1000); // Check every second
            timer.Elapsed += (sender, e) =>
            {
                string currentTime = DateTime.Now.ToString("HH:mm:ss");
                if (currentTime == userTime)
                {
                    // Raise the event
                    OnRaiseAlarm(EventArgs.Empty);
                    timer.Stop(); // Stop the timer after the alarm is triggered
                    alarmTriggered.Set(); // Signal that the alarm has been triggered
                }
            };
            timer.Start();
        }

        // Protected method to raise the event
        protected virtual void OnRaiseAlarm(EventArgs e)
        {
            RaiseAlarm?.Invoke(this, e);
        }
    }

    // Subscriber class
    public class AlarmSubscriber
    {
        // Method to handle the event
        public void RingAlarm(object? sender, EventArgs e)
        {
            Console.WriteLine("Alarm! The specified time has been reached.");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the time in HH:mm:ss format:");
            string userTime = Console.ReadLine() ?? string.Empty;

            // Validate the input time format
            if (!TimeSpan.TryParse(userTime, out _))
            {
                Console.WriteLine("Invalid time format. Please use HH:mm:ss.");
                return;
            }

            // Create instances of publisher and subscriber
            AlarmClock alarmClock = new AlarmClock();
            AlarmSubscriber subscriber = new AlarmSubscriber();

            // Subscribe to the event
            alarmClock.RaiseAlarm += subscriber.RingAlarm;

            // Create a ManualResetEvent to wait for the alarm
            ManualResetEvent alarmTriggered = new ManualResetEvent(false);

            Console.WriteLine("Waiting for the specified time...");
            alarmClock.CheckTime(userTime, alarmTriggered);

            // Wait for the alarm to be triggered
            alarmTriggered.WaitOne();

            // Prompt the user to press any key to exit
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }
    }
}
