namespace Alarmclock
{
    partial class Form1
    {
        private System.ComponentModel.IContainer components = null;
        private System.Windows.Forms.TextBox txtTimeInput;
        private System.Windows.Forms.Button btnStart;
        private System.Windows.Forms.Timer timer;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.txtTimeInput = new System.Windows.Forms.TextBox();
            this.btnStart = new System.Windows.Forms.Button();
            this.timer = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();

            // TextBox
            this.txtTimeInput.Location = new System.Drawing.Point(50, 30);
            this.txtTimeInput.Name = "txtTimeInput";
            this.txtTimeInput.Size = new System.Drawing.Size(200, 23);
            this.txtTimeInput.TabIndex = 0;
            this.txtTimeInput.PlaceholderText = "Enter time (HH:MM:SS)";

            // Button
            this.btnStart.Location = new System.Drawing.Point(50, 70);
            this.btnStart.Name = "btnStart";
            this.btnStart.Size = new System.Drawing.Size(200, 30);
            this.btnStart.TabIndex = 1;
            this.btnStart.Text = "Start";
            this.btnStart.UseVisualStyleBackColor = true;
            this.btnStart.Click += new System.EventHandler(this.btnStart_Click);

            // Form1
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(300, 150);
            this.Controls.Add(this.txtTimeInput);
            this.Controls.Add(this.btnStart);
            this.Name = "Form1";
            this.Text = "Alarm Clock";
            this.ResumeLayout(false);
            this.PerformLayout();
        }
    }
}
