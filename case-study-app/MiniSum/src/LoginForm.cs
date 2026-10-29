using System;
using System.Drawing;
using System.Windows.Forms;

namespace MiniSum
{
    /// <summary>
    /// Màn hình 1: Đăng nhập.
    /// Tài khoản hợp lệ: admin / 1234 (theo đặc tả T03 trong ke_hoach_lan2.md).
    /// AutomationId: winLogin, txtUser, txtPass, btnLogin, lblMessage.
    ///
    /// Giao diện theo phong cách Fluent Light (xem Theme.cs). Chỉ phần trình bày thay đổi,
    /// toàn bộ AutomationId / loại control / chuỗi thông điệp giữ nguyên cho automation.
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
            ClientSize = new Size(460, 518);
            StartPosition = FormStartPosition.CenterScreen;
            FormBorderStyle = FormBorderStyle.FixedSingle;
            MaximizeBox = false;
            Font = Theme.Body();
            BackColor = Theme.Canvas;
            DoubleBuffered = true;

            // ----- Phần trang trí (không mang AutomationId, không ảnh hưởng locator) -----
            var accent = Theme.CreateAccentStrip(ClientSize.Width);
            var brandMark = Theme.CreateBrandMark();
            brandMark.Location = new Point(40, 32);

            var lblTitle = new Label
            {
                Name = "lblTitle",
                Text = "MiniSum",
                AutoSize = true,
                Font = Theme.Title(22F),
                ForeColor = Theme.TextPrimary,
                BackColor = Theme.Canvas,
                Location = new Point(102, 38)
            };

            var lblSubtitle = new Label
            {
                Name = "lblSubtitle",
                Text = "Automation Testing Demo",
                AutoSize = true,
                Font = Theme.Body(9.5F),
                ForeColor = Theme.TextSecondary,
                BackColor = Theme.Canvas,
                Location = new Point(104, 74)
            };

            // ----- Card trắng chứa form đăng nhập -----
            var card = Theme.CreateCard(14);
            card.Location = new Point(24, 118);
            card.Size = new Size(412, 320);

            var lblUser = Theme.CreateCaption("TÀI KHOẢN");
            lblUser.Name = "lblUser";
            lblUser.Location = new Point(24, 24);

            txtUser = new TextBox { Name = "txtUser" };
            txtUser.AccessibleName = "Tai khoan:";
            var userShell = Theme.CreateInputShell(txtUser);
            userShell.Location = new Point(24, 52);
            userShell.Size = new Size(364, 44);
            userShell.TabIndex = 0;

            var lblPass = Theme.CreateCaption("MẬT KHẨU");
            lblPass.Name = "lblPass";
            lblPass.Location = new Point(24, 112);

            txtPass = new TextBox
            {
                Name = "txtPass",
                UseSystemPasswordChar = true
            };
            txtPass.AccessibleName = "Mat khau:";
            var passShell = Theme.CreateInputShell(txtPass);
            passShell.Location = new Point(24, 140);
            passShell.Size = new Size(364, 44);
            passShell.TabIndex = 1;

            btnLogin = new Button
            {
                Name = "btnLogin",
                Text = "DANG NHAP",
                Location = new Point(24, 204),
                Size = new Size(364, 46),
                TabIndex = 2
            };
            Theme.StylePrimaryButton(btnLogin);
            btnLogin.Click += BtnLogin_Click;

            lblMessage = new Label
            {
                Name = "lblMessage",
                Text = string.Empty,
                ForeColor = Theme.Danger,
                BackColor = Theme.Surface,
                Location = new Point(24, 258),
                Size = new Size(364, 38),
                Font = Theme.Body(10F),
                TextAlign = ContentAlignment.TopLeft,
                TabIndex = 3
            };

            card.Controls.Add(lblUser);
            card.Controls.Add(userShell);
            card.Controls.Add(lblPass);
            card.Controls.Add(passShell);
            card.Controls.Add(btnLogin);
            card.Controls.Add(lblMessage);

            // ----- Chân trang -----
            var lblBuild = new Label
            {
                Name = "lblBuild",
                Text = Theme.BuildLabel,
                AutoSize = true,
                Font = Theme.Body(9F),
                ForeColor = Theme.TextMuted,
                BackColor = Theme.Canvas,
                Location = new Point(40, 464)
            };

            var lblHint = new Label
            {
                Name = "lblHint",
                Text = "Tai khoan demo: admin / 1234",
                AutoSize = false,
                Size = new Size(240, 18),
                TextAlign = ContentAlignment.MiddleRight,
                Font = Theme.Body(9F),
                ForeColor = Theme.TextMuted,
                BackColor = Theme.Canvas,
                Location = new Point(172, 464)
            };

            AcceptButton = btnLogin;
            Controls.Add(accent);
            Controls.Add(brandMark);
            Controls.Add(lblTitle);
            Controls.Add(lblSubtitle);
            Controls.Add(card);
            Controls.Add(lblBuild);
            Controls.Add(lblHint);

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
                lblMessage.ForeColor = Theme.Success;
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
            lblMessage.ForeColor = Theme.Danger;
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
