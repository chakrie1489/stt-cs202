using System;
using System.Drawing;
using System.Windows.Forms;

namespace Alarmclock
{
    public partial class Form1 : Form
    {
        private DateTime targetTime;
        private Random random = new Random();

        public Form1()
        {
            InitializeComponent();
        }

        private void btnStart_Click(object sender, EventArgs e)
        {
            // Parse and validate input (validation left as an exercise)
            if (DateTime.TryParseExact(txtTimeInput.Text, "HH:mm:ss", null, System.Globalization.DateTimeStyles.None, out targetTime))
            {
                targetTime = DateTime.Today.Add(targetTime.TimeOfDay); // Set target time for today
                timer.Interval = 1000; // 1 second
                timer.Tick += Timer_Tick;
                timer.Start();
            }
            else
            {
                MessageBox.Show("Invalid time format. Please enter in HH:MM:SS format.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void Timer_Tick(object sender, EventArgs e)
        {
            // Change background color
            this.BackColor = Color.FromArgb(random.Next(256), random.Next(256), random.Next(256));

            // Check if target time is reached
            if (DateTime.Now >= targetTime)
            {
                timer.Stop();
                MessageBox.Show("Target time reached!", "Alarm", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }
    }
}

