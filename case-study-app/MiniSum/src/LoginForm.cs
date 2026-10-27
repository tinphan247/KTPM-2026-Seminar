using System;
using System.Drawing;
using System.Windows.Forms;

namespace MiniSum
{
    /// <summary>
    /// Màn hình 1: Đăng nhập.
    /// Tài khoản hợp lệ: admin / 1234 (theo đặc tả T03 trong ke_hoach_lan2.md).
    /// AutomationId: winLogin, txtUser, txtPass, btnLogin, lblMessage.
    /// </summary>
    public class LoginForm : Form
    {
        internal const string ValidUser = "admin";
        internal const string ValidPass = "1234";

        private const int SuccessDelayMs = 1000;

        private readonly TextBox txtUser;
        private readonly TextBox txtPass;
        private readonly Button btnLogin;
        private readonly Label lblMessage;

        private Timer transitionTimer;

        public LoginForm()
        {
            Name = "winLogin";
            Text = "MiniSum - Dang nhap";
            ClientSize = new Size(400, 300);
            StartPosition = FormStartPosition.CenterScreen;
            FormBorderStyle = FormBorderStyle.FixedSingle;
            MaximizeBox = false;
            Font = new Font("Segoe UI", 10F);
            BackColor = Color.White;

            var lblTitle = new Label
            {
                Name = "lblTitle",
                Text = "MiniSum - Dang nhap",
                Font = new Font("Segoe UI", 14F, FontStyle.Bold),
                ForeColor = Color.Black,
                AutoSize = true,
                Location = new Point(30, 20)
            };

            var lblUser = new Label
            {
                Name = "lblUser",
                Text = "Tai khoan:",
                AutoSize = true,
                Location = new Point(30, 72)
            };

            txtUser = new TextBox
            {
                Name = "txtUser",
                Location = new Point(140, 69),
                Size = new Size(210, 25)
            };

            var lblPass = new Label
            {
                Name = "lblPass",
                Text = "Mat khau:",
                AutoSize = true,
                Location = new Point(30, 112)
            };

            txtPass = new TextBox
            {
                Name = "txtPass",
                Location = new Point(140, 109),
                Size = new Size(210, 25),
                UseSystemPasswordChar = true
            };

            btnLogin = new Button
            {
                Name = "btnLogin",
                Text = "DANG NHAP",
                Location = new Point(140, 152),
                Size = new Size(210, 36),
                BackColor = Color.FromArgb(0, 120, 215),
                ForeColor = Color.White,
                FlatStyle = FlatStyle.Flat
            };
            btnLogin.Click += BtnLogin_Click;

            lblMessage = new Label
            {
                Name = "lblMessage",
                Text = string.Empty,
                ForeColor = Color.DarkOrange,
                Location = new Point(30, 205),
                Size = new Size(340, 50)
            };

            AcceptButton = btnLogin;
            Controls.Add(lblTitle);
            Controls.Add(lblUser);
            Controls.Add(txtUser);
            Controls.Add(lblPass);
            Controls.Add(txtPass);
            Controls.Add(btnLogin);
            Controls.Add(lblMessage);

            Shown += (sender, e) => txtUser.Focus();
        }

        /// <summary>
        /// Đưa form về trạng thái ban đầu khi người dùng đăng xuất từ màn hình tính toán.
        /// </summary>
        internal void PrepareForReuse()
        {
            if (transitionTimer != null)
            {
                transitionTimer.Stop();
                transitionTimer.Dispose();
                transitionTimer = null;
            }

            txtUser.Clear();
            txtPass.Clear();
            lblMessage.Text = string.Empty;
            btnLogin.Enabled = true;
            txtUser.Focus();
        }

        private void BtnLogin_Click(object sender, EventArgs e)
        {
            string user = txtUser.Text.Trim();
            string pass = txtPass.Text;

            if (user.Length == 0 && pass.Length == 0)
            {
                ShowError("Vui long nhap tai khoan va mat khau");
                return;
            }

            if (user.Length == 0)
            {
                ShowError("Ten dang nhap khong duoc de trong");
                return;
            }

            if (pass.Length == 0)
            {
                ShowError("Mat khau khong duoc de trong");
                return;
            }

            if (user == ValidUser && pass == ValidPass)
            {
                lblMessage.ForeColor = Color.Green;
                lblMessage.Text = "Dang nhap thanh cong";
                btnLogin.Enabled = false;
                StartTransition();
                return;
            }

            txtPass.Clear();
            ShowError("Sai tai khoan hoac mat khau");
        }

        private void ShowError(string message)
        {
            lblMessage.ForeColor = Color.DarkOrange;
            lblMessage.Text = message;
        }

        /// <summary>
        /// Giữ thông báo thành công trên màn hình một khoảng ngắn để test runner
        /// kịp đọc checkpoint lblMessage trước khi chuyển màn hình.
        /// </summary>
        private void StartTransition()
        {
            transitionTimer = new Timer { Interval = SuccessDelayMs };
            transitionTimer.Tick += TransitionTimer_Tick;
            transitionTimer.Start();
        }

        private void TransitionTimer_Tick(object sender, EventArgs e)
        {
            transitionTimer.Stop();
            transitionTimer.Dispose();
            transitionTimer = null;

            var calculator = new CalculatorForm(this);
            calculator.Show();
            Hide();
        }
    }
}
