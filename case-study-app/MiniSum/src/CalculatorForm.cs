using System;
using System.Drawing;
using System.Windows.Forms;

namespace MiniSum
{
    /// <summary>
    /// Màn hình 2: Tính tổng A + B.
    ///
    /// Khác biệt theo phiên bản (xem case-study-app/README.md):
    ///   v1: nút AutomationId = btnSum, không có kiểm tra dữ liệu.
    ///   v2: nút đổi thành btnCalculate + màn hình Lịch sử (demo maintenance).
    ///   v3: giữ btnSum, thêm validation và nhãn lỗi lblError (demo negative test).
    /// </summary>
    public class CalculatorForm : Form
    {
        private const int LowerBound = -99;
        private const int UpperBound = 99;

#if V2
        private const string SumButtonAutomationId = "btnCalculate";
#else
        private const string SumButtonAutomationId = "btnSum";
#endif

        private readonly LoginForm loginForm;
        private readonly TextBox txtA;
        private readonly TextBox txtB;
        private readonly Button btnSum;
        private readonly Button btnLogout;
        private readonly Label lblResult;

#if V2
        private readonly Button btnHistory;
#endif

#if V3
        private readonly Label lblError;
#endif

        internal CalculatorForm(LoginForm loginForm)
        {
            this.loginForm = loginForm;

            Name = "winMain";
            Text = "MiniSum - Tinh tong";
            ClientSize = new Size(440, 320);
            StartPosition = FormStartPosition.CenterScreen;
            FormBorderStyle = FormBorderStyle.FixedSingle;
            MaximizeBox = false;
            Font = new Font("Segoe UI", 10F);
            BackColor = Color.White;

            var lblA = new Label
            {
                Name = "lblA",
                Text = "So A:",
                AutoSize = true,
                Location = new Point(30, 30)
            };

            txtA = new TextBox
            {
                Name = "txtA",
                Location = new Point(140, 27),
                Size = new Size(160, 25)
            };

            var lblB = new Label
            {
                Name = "lblB",
                Text = "So B:",
                AutoSize = true,
                Location = new Point(30, 70)
            };

            txtB = new TextBox
            {
                Name = "txtB",
                Location = new Point(140, 67),
                Size = new Size(160, 25)
            };

            btnSum = new Button
            {
                Name = SumButtonAutomationId,
                Text = "TINH TONG",
                Location = new Point(140, 110),
                Size = new Size(160, 36),
                BackColor = Color.FromArgb(0, 120, 215),
                ForeColor = Color.White,
                FlatStyle = FlatStyle.Flat
            };
            btnSum.Click += BtnSum_Click;

            lblResult = new Label
            {
                Name = "lblResult",
                Text = string.Empty,
                Location = new Point(30, 170),
                Size = new Size(380, 25),
                ForeColor = Color.FromArgb(0, 100, 0)
            };

#if V2
            btnHistory = new Button
            {
                Name = "btnHistory",
                Text = "LICH SU",
                Location = new Point(310, 110),
                Size = new Size(100, 36),
                FlatStyle = FlatStyle.Flat
            };
            btnHistory.Click += BtnHistory_Click;
#endif

#if V3
            lblError = new Label
            {
                Name = "lblError",
                Text = string.Empty,
                Location = new Point(30, 205),
                Size = new Size(380, 45),
                ForeColor = Color.Firebrick
            };
#endif

            btnLogout = new Button
            {
                Name = "btnLogout",
                Text = "DANG XUAT",
                Location = new Point(310, 265),
                Size = new Size(100, 32),
                FlatStyle = FlatStyle.Flat
            };
            btnLogout.Click += BtnLogout_Click;

            AcceptButton = btnSum;
            Controls.Add(lblA);
            Controls.Add(txtA);
            Controls.Add(lblB);
            Controls.Add(txtB);
            Controls.Add(btnSum);
            Controls.Add(lblResult);
            Controls.Add(btnLogout);
#if V2
            Controls.Add(btnHistory);
#endif
#if V3
            Controls.Add(lblError);
#endif

            Shown += (sender, e) => txtA.Focus();
        }

        private void BtnSum_Click(object sender, EventArgs e)
        {
            string rawA = txtA.Text.Trim();
            string rawB = txtB.Text.Trim();

            lblResult.Text = string.Empty;
#if V3
            lblError.Text = string.Empty;

            if (rawA.Length == 0 || rawB.Length == 0)
            {
                ShowError("Vui long nhap day du gia tri A va B");
                return;
            }

            if (!int.TryParse(rawA, out int a) || !int.TryParse(rawB, out int b))
            {
                ShowError("Gia tri khong hop le: phai la so nguyen");
                return;
            }

            if (a < LowerBound || a > UpperBound)
            {
                ShowError($"A ngoai mien [{LowerBound}, {UpperBound}]");
                return;
            }

            if (b < LowerBound || b > UpperBound)
            {
                ShowError($"B ngoai mien [{LowerBound}, {UpperBound}]");
                return;
            }

            ShowResult(a, b);
#else
            if (!int.TryParse(rawA, out int a) || !int.TryParse(rawB, out int b))
            {
                // v1/v2 chưa có validation: chỉ báo chung chung trên nhãn kết quả.
                lblResult.Text = "Nhap sai dinh dang";
                return;
            }

            ShowResult(a, b);
#endif
        }

        private void ShowResult(int a, int b)
        {
            int sum = a + b;
            lblResult.Text = $"Ket qua: {a} + {b} = {sum}";

#if V2
            CalculationHistory.Add($"{DateTime.Now:HH:mm:ss}   {a} + {b} = {sum}");
#endif
        }

#if V3
        private void ShowError(string message)
        {
            lblError.Text = message;
        }
#endif

#if V2
        private void BtnHistory_Click(object sender, EventArgs e)
        {
            // Hiển thị dạng modeless để thao tác mở cửa sổ không chặn luồng automation.
            var history = new HistoryForm();
            history.Show(this);
        }
#endif

        private void BtnLogout_Click(object sender, EventArgs e)
        {
            loginForm.PrepareForReuse();
            loginForm.Show();
            Close();
        }
    }
}
