using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Text;
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
    ///
    /// Giao diện theo phong cách Fluent Light (xem Theme.cs). Chỉ phần trình bày thay đổi,
    /// AutomationId / loại control / chuỗi kết quả giữ nguyên cho automation.
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

        // Kích thước cửa sổ khác nhau vì v3 có thêm banner lỗi lblError.
#if V3
        private const int FormHeight = 610;
        private const int CardHeight = 430;
        private const int FooterTop = 556;
#else
        private const int FormHeight = 538;
        private const int CardHeight = 358;
        private const int FooterTop = 484;
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
        private Panel errorPanel;
        private bool hasError;
#endif

        internal CalculatorForm(LoginForm loginForm)
        {
            this.loginForm = loginForm;

            Name = "winMain";
            Text = "MiniSum - Tinh tong";
            ClientSize = new Size(500, FormHeight);
            StartPosition = FormStartPosition.CenterScreen;
            FormBorderStyle = FormBorderStyle.FixedSingle;
            MaximizeBox = false;
            Font = Theme.Body();
            BackColor = Theme.Canvas;
            DoubleBuffered = true;

            // ----- Phần trang trí -----
            var accent = Theme.CreateAccentStrip(ClientSize.Width);

            var lblTitle = new Label
            {
                Name = "lblTitle",
                Text = "Tính tổng",
                AutoSize = true,
                Font = Theme.Title(20F),
                ForeColor = Theme.TextPrimary,
                BackColor = Theme.Canvas,
                Location = new Point(38, 26)
            };

            var lblSubtitle = new Label
            {
                Name = "lblSubtitle",
                Text = "Nhập hai số nguyên trong [-99, 99]",
                AutoSize = true,
                Font = Theme.Body(10F),
                ForeColor = Theme.TextSecondary,
                BackColor = Theme.Canvas,
                Location = new Point(41, 74)
            };

            // ----- Card trắng -----
            var card = Theme.CreateCard(14);
            card.Location = new Point(24, 106);
            card.Size = new Size(452, CardHeight);

            var lblA = Theme.CreateCaption("Số A");
            lblA.Name = "lblA";
            lblA.Location = new Point(24, 24);

            txtA = new TextBox { Name = "txtA" };
            txtA.AccessibleName = "So A:";
            var shellA = Theme.CreateInputShell(txtA);
            shellA.Location = new Point(24, 52);
            shellA.Size = new Size(188, 44);
            shellA.TabIndex = 0;

            var lblB = Theme.CreateCaption("Số B");
            lblB.Name = "lblB";
            lblB.Location = new Point(240, 24);

            txtB = new TextBox { Name = "txtB" };
            txtB.AccessibleName = "So B:";
            var shellB = Theme.CreateInputShell(txtB);
            shellB.Location = new Point(240, 52);
            shellB.Size = new Size(188, 44);
            shellB.TabIndex = 1;

            btnSum = new Button
            {
                Name = SumButtonAutomationId,
                Text = "TINH TONG",
                Location = new Point(24, 116),
                Size = new Size(404, 46),
                TabIndex = 2
            };
            Theme.StylePrimaryButton(btnSum);
            btnSum.Click += BtnSum_Click;

            // ----- Khối kết quả -----
            var resultPanel = Theme.CreateTintedPanel(Theme.ResultSurface, Theme.ResultBorder, 10);
            resultPanel.BackColor = Theme.Surface;
            resultPanel.Location = new Point(24, 182);
            resultPanel.Size = new Size(404, 86);
            resultPanel.Paint += (sender, e) =>
            {
                // Nhãn "KẾT QUẢ" được vẽ trực tiếp để không tạo thêm Label:
                // nếu có Label đứng trước, WinForms sẽ gán tên của nó cho lblResult rỗng.
                e.Graphics.TextRenderingHint = TextRenderingHint.ClearTypeGridFit;
                using (var font = Theme.Caption(9F))
                using (var brush = new SolidBrush(Theme.TextSecondary))
                {
                    e.Graphics.DrawString("KẾT QUẢ", font, brush, 16, 12);
                }
            };

            lblResult = new Label
            {
                Name = "lblResult",
                Text = string.Empty,
                AutoSize = false,
                Size = new Size(372, 32),
                Location = new Point(16, 34),
                Font = Theme.Result(14F),
                ForeColor = Theme.Primary,
                BackColor = Theme.ResultSurface,
                TextAlign = ContentAlignment.MiddleLeft
            };

            resultPanel.Controls.Add(lblResult);

#if V3
            // ----- Banner lỗi (chỉ v3) -----
            // Banner chỉ hiện nền đỏ khi thật sự có lỗi; khi rỗng thì hoà vào nền card.
            // lblError luôn Visible để automation luôn tìm thấy AutomationId.
            errorPanel = new Panel
            {
                BackColor = Theme.Surface,
                Location = new Point(24, 284),
                Size = new Size(404, 56)
            };
            errorPanel.Paint += (sender, e) =>
            {
                if (!hasError)
                {
                    return;
                }

                e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
                e.Graphics.TextRenderingHint = TextRenderingHint.ClearTypeGridFit;

                var rect = new Rectangle(0, 0, errorPanel.Width - 1, errorPanel.Height - 1);
                using (var path = Theme.RoundedPath(rect, 10))
                using (var fill = new SolidBrush(Theme.DangerSurface))
                using (var pen = new Pen(Theme.DangerBorder))
                {
                    e.Graphics.FillPath(fill, path);
                    e.Graphics.DrawPath(pen, path);
                }

                // Biểu tượng "!" vẽ trực tiếp (không dùng Label) để không ảnh hưởng tên của lblError.
                var circle = new Rectangle(16, 18, 20, 20);
                using (var brush = new SolidBrush(Theme.Danger))
                {
                    e.Graphics.FillEllipse(brush, circle);
                }

                using (var font = new Font(Theme.FontFamily, 10F, FontStyle.Bold))
                using (var textBrush = new SolidBrush(Color.White))
                using (var format = new StringFormat
                {
                    Alignment = StringAlignment.Center,
                    LineAlignment = StringAlignment.Center
                })
                {
                    e.Graphics.DrawString("!", font, textBrush,
                        new RectangleF(circle.X, circle.Y - 1, circle.Width, circle.Height), format);
                }
            };

            lblError = new Label
            {
                Name = "lblError",
                Text = string.Empty,
                AutoSize = false,
                Size = new Size(352, 36),
                Location = new Point(44, 10),
                Font = Theme.Body(9.5F),
                ForeColor = Theme.Danger,
                BackColor = Theme.Surface,
                TextAlign = ContentAlignment.MiddleLeft
            };

            errorPanel.Controls.Add(lblError);
#endif

            // ----- Hàng nút thao tác -----
            int actionTop = CardHeight - 70;

#if V2
            btnHistory = new Button
            {
                Name = "btnHistory",
                Text = "LICH SU",
                Location = new Point(24, actionTop),
                Size = new Size(196, 46),
                TabIndex = 3
            };
            Theme.StyleSecondaryButton(btnHistory);
            btnHistory.Click += BtnHistory_Click;
#endif

            btnLogout = new Button
            {
                Name = "btnLogout",
                Text = "DANG XUAT",
                Location = new Point(232, actionTop),
                Size = new Size(196, 46),
#if V2
                TabIndex = 4
#else
                TabIndex = 3
#endif
            };
            Theme.StyleSecondaryButton(btnLogout);
            btnLogout.Click += BtnLogout_Click;

            card.Controls.Add(lblA);
            card.Controls.Add(shellA);
            card.Controls.Add(lblB);
            card.Controls.Add(shellB);
            card.Controls.Add(btnSum);
            card.Controls.Add(resultPanel);
#if V3
            card.Controls.Add(errorPanel);
#endif
#if V2
            card.Controls.Add(btnHistory);
#endif
            card.Controls.Add(btnLogout);

            var lblFooter = new Label
            {
                Name = "lblFooter",
                Text = Theme.BuildLabel,
                AutoSize = true,
                Font = Theme.Body(9F),
                ForeColor = Theme.TextMuted,
                BackColor = Theme.Canvas,
                Location = new Point(40, FooterTop)
            };

            var lblFooterHint = new Label
            {
                Name = "lblFooterHint",
                Text = "Nhấn Enter để tính nhanh",
                AutoSize = false,
                Size = new Size(240, 18),
                TextAlign = ContentAlignment.MiddleRight,
                Font = Theme.Body(9F),
                ForeColor = Theme.TextMuted,
                BackColor = Theme.Canvas,
                Location = new Point(212, FooterTop)
            };

            AcceptButton = btnSum;
            Controls.Add(accent);
            Controls.Add(lblTitle);
            Controls.Add(lblSubtitle);
            Controls.Add(card);
            Controls.Add(lblFooter);
            Controls.Add(lblFooterHint);

            Shown += (sender, e) => txtA.Focus();
        }

        private void BtnSum_Click(object sender, EventArgs e)
        {
            string rawA = txtA.Text.Trim();
            string rawB = txtB.Text.Trim();

            lblResult.Text = string.Empty;
            lblResult.ForeColor = Theme.Primary;
#if V3
            lblError.Text = string.Empty;
            SetErrorBannerVisible(false);

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
                lblResult.ForeColor = Theme.Danger;
                lblResult.Text = "Nhap sai dinh dang";
                return;
            }

            ShowResult(a, b);
#endif
        }

        private void ShowResult(int a, int b)
        {
            int sum = a + b;
            lblResult.ForeColor = Theme.Primary;
            lblResult.Text = $"Ket qua: {a} + {b} = {sum}";

#if V2
            CalculationHistory.Add($"{DateTime.Now:HH:mm:ss}   {a} + {b} = {sum}");
#endif
        }

#if V3
        private void ShowError(string message)
        {
            lblError.Text = message;
            SetErrorBannerVisible(true);
        }

        private void SetErrorBannerVisible(bool visible)
        {
            if (hasError == visible)
            {
                return;
            }

            hasError = visible;
            lblError.BackColor = visible ? Theme.DangerSurface : Theme.Surface;
            errorPanel.Invalidate();
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
