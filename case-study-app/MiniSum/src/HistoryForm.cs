using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace MiniSum
{
    /// <summary>
    /// Màn hình Lịch sử tính toán (chỉ có ở phiên bản v2).
    /// AutomationId: winHistory, lstHistory, btnClose.
    /// </summary>
    public class HistoryForm : Form
    {
        public HistoryForm()
        {
            Name = "winHistory";
            Text = "MiniSum - Lich su tinh toan";
            ClientSize = new Size(400, 320);
            StartPosition = FormStartPosition.CenterParent;
            FormBorderStyle = FormBorderStyle.FixedDialog;
            MaximizeBox = false;
            MinimizeBox = false;
            Font = new Font("Segoe UI", 10F);
            BackColor = Color.White;

            var lstHistory = new ListBox
            {
                Name = "lstHistory",
                Location = new Point(20, 20),
                Size = new Size(360, 225),
                Font = new Font("Consolas", 10F)
            };

            IReadOnlyList<string> entries = CalculationHistory.Snapshot();
            if (entries.Count == 0)
            {
                lstHistory.Items.Add("(Chua co phep tinh nao)");
            }
            else
            {
                foreach (string entry in entries)
                {
                    lstHistory.Items.Add(entry);
                }
            }

            var btnClose = new Button
            {
                Name = "btnClose",
                Text = "DONG",
                Location = new Point(280, 262),
                Size = new Size(100, 32),
                FlatStyle = FlatStyle.Flat
            };
            btnClose.Click += (sender, e) => Close();

            CancelButton = btnClose;
            Controls.Add(lstHistory);
            Controls.Add(btnClose);
        }
    }
}
