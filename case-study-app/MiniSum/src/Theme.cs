using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;

namespace MiniSum
{
    /// <summary>
    /// Bảng màu, font và các helper dựng giao diện dùng chung cho cả 3 phiên bản.
    ///
    /// Nguyên tắc: chỉ thay đổi phần trình bày. AutomationId (thuộc tính Name),
    /// loại control và nội dung nghiệp vụ của MiniSum giữ nguyên để không ảnh hưởng
    /// script Katalon Studio / WinAppDriver.
    /// </summary>
    internal static class Theme
    {
        internal const string FontFamily = "Segoe UI";

        // Bảng màu Fluent Light
        internal static readonly Color Canvas = FromHex("#F3F6FB");
        internal static readonly Color Surface = FromHex("#FFFFFF");
        internal static readonly Color Border = FromHex("#E2E8F0");
        internal static readonly Color BorderStrong = FromHex("#CBD5E1");
        internal static readonly Color Primary = FromHex("#2563EB");
        internal static readonly Color PrimaryHover = FromHex("#1D4ED8");
        internal static readonly Color PrimaryPressed = FromHex("#1E40AF");

        internal static readonly Color TextPrimary = FromHex("#0F172A");
        internal static readonly Color TextSecondary = FromHex("#64748B");
        internal static readonly Color TextMuted = FromHex("#94A3B8");

        internal static readonly Color Success = FromHex("#16A34A");
        internal static readonly Color Danger = FromHex("#DC2626");
        internal static readonly Color DangerSurface = FromHex("#FEF2F2");
        internal static readonly Color DangerBorder = FromHex("#FECACA");
        internal static readonly Color ResultSurface = FromHex("#EFF6FF");
        internal static readonly Color ResultBorder = FromHex("#DBEAFE");
        internal static readonly Color RowAlt = FromHex("#F8FAFC");
        internal static readonly Color SecondarySurface = FromHex("#EEF2F7");
        internal static readonly Color SecondaryHover = FromHex("#E2E8F0");

#if V2
        internal const string BuildLabel = "MiniSum v2  ·  WinForms .NET 8";
#elif V3
        internal const string BuildLabel = "MiniSum v3  ·  WinForms .NET 8";
#else
        internal const string BuildLabel = "MiniSum v1  ·  WinForms .NET 8";
#endif

        internal static Color FromHex(string hex)
        {
            return ColorTranslator.FromHtml(hex);
        }

        // ---------- Typography ----------

        internal static Font Title(float size = 20F)
        {
            return new Font(FontFamily, size, FontStyle.Bold);
        }

        internal static Font Subtitle(float size = 10F)
        {
            return new Font(FontFamily, size, FontStyle.Regular);
        }

        internal static Font Body(float size = 10.5F)
        {
            return new Font(FontFamily, size, FontStyle.Regular);
        }

        internal static Font Caption(float size = 9.5F)
        {
            return new Font(FontFamily, size, FontStyle.Bold);
        }

        internal static Font Result(float size = 15F)
        {
            return new Font(FontFamily, size, FontStyle.Bold);
        }

        // ---------- Hình khối ----------

        internal static GraphicsPath RoundedPath(Rectangle bounds, int radius)
        {
            var path = new GraphicsPath();
            int diameter = radius * 2;

            path.AddArc(bounds.X, bounds.Y, diameter, diameter, 180, 90);
            path.AddArc(bounds.Right - diameter, bounds.Y, diameter, diameter, 270, 90);
            path.AddArc(bounds.Right - diameter, bounds.Bottom - diameter, diameter, diameter, 0, 90);
            path.AddArc(bounds.X, bounds.Bottom - diameter, diameter, diameter, 90, 90);
            path.CloseFigure();

            return path;
        }

        internal static void ApplyRoundedRegion(Control control, int radius)
        {
            if (control.Width <= 0 || control.Height <= 0)
            {
                return;
            }

            using (var path = RoundedPath(new Rectangle(0, 0, control.Width, control.Height), radius))
            {
                control.Region = new Region(path);
            }
        }

        /// <summary>
        /// Dải màu nhấn ở mép trên cửa sổ.
        /// </summary>
        internal static Panel CreateAccentStrip(int width)
        {
            var strip = new Panel
            {
                Location = new Point(0, 0),
                Size = new Size(width, 6),
                BackColor = Primary
            };

            strip.Paint += (sender, e) =>
            {
                using (var brush = new LinearGradientBrush(
                    strip.ClientRectangle, Primary, FromHex("#7C3AED"), LinearGradientMode.Horizontal))
                {
                    e.Graphics.FillRectangle(brush, strip.ClientRectangle);
                }
            };

            return strip;
        }

        /// <summary>
        /// Ô vuông gradient có chữ Σ – dùng làm logo nhỏ ở màn hình đăng nhập.
        /// </summary>
        internal static Panel CreateBrandMark(int size = 48)
        {
            var mark = new Panel
            {
                Size = new Size(size, size),
                BackColor = Canvas
            };

            mark.Paint += (sender, e) =>
            {
                e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
                var rect = new Rectangle(0, 0, mark.Width - 1, mark.Height - 1);

                using (var path = RoundedPath(rect, 12))
                using (var brush = new LinearGradientBrush(rect, Primary, FromHex("#7C3AED"), LinearGradientMode.ForwardDiagonal))
                {
                    e.Graphics.FillPath(brush, path);
                }

                using (var font = new Font(FontFamily, 18F, FontStyle.Bold))
                using (var format = new StringFormat
                {
                    Alignment = StringAlignment.Center,
                    LineAlignment = StringAlignment.Center
                })
                using (var textBrush = new SolidBrush(Color.White))
                {
                    e.Graphics.DrawString("Σ", font, textBrush,
                        new RectangleF(0, 0, mark.Width, mark.Height), format);
                }
            };

            return mark;
        }

        /// <summary>
        /// Card trắng bo góc đặt trên nền canvas.
        /// Lưu ý: control con đặt trên card cần BackColor = Surface để hoà vào nền card.
        /// </summary>
        internal static Panel CreateCard(int radius = 12)
        {
            var card = new Panel { BackColor = Canvas };

            card.Paint += (sender, e) =>
            {
                e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
                var rect = new Rectangle(0, 0, card.Width - 1, card.Height - 1);
                using (var path = RoundedPath(rect, radius))
                using (var fill = new SolidBrush(Surface))
                using (var pen = new Pen(Border))
                {
                    e.Graphics.FillPath(fill, path);
                    e.Graphics.DrawPath(pen, path);
                }
            };

            return card;
        }

        /// <summary>
        /// Khung bo góc có màu nền riêng (dùng cho khối kết quả, banner lỗi).
        /// </summary>
        internal static Panel CreateTintedPanel(Color fillColor, Color borderColor, int radius = 10)
        {
            var panel = new Panel { BackColor = Canvas };

            panel.Paint += (sender, e) =>
            {
                e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
                var rect = new Rectangle(0, 0, panel.Width - 1, panel.Height - 1);
                using (var path = RoundedPath(rect, radius))
                using (var fill = new SolidBrush(fillColor))
                using (var pen = new Pen(borderColor))
                {
                    e.Graphics.FillPath(fill, path);
                    e.Graphics.DrawPath(pen, path);
                }
            };

            return panel;
        }

        // ---------- Ô nhập liệu ----------
        /// <summary>
        /// Bọc TextBox trong khung bo góc, viền đổi màu khi focus.
        /// TextBox bên trong vẫn là control chuẩn (AutomationId + ValuePattern giữ nguyên).
        /// </summary>
        internal static Panel CreateInputShell(TextBox textBox)
        {
            var shell = new Panel
            {
                BackColor = Surface,
                Padding = new Padding(12, 9, 12, 9)
            };

            textBox.BorderStyle = BorderStyle.None;
            textBox.BackColor = Surface;
            textBox.ForeColor = TextPrimary;
            textBox.Font = Body(11F);
            textBox.Dock = DockStyle.Fill;

            bool focused = false;
            textBox.Enter += (sender, e) => { focused = true; shell.Invalidate(); };
            textBox.Leave += (sender, e) => { focused = false; shell.Invalidate(); };

            shell.Paint += (sender, e) =>
            {
                e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
                var rect = new Rectangle(0, 0, shell.Width - 1, shell.Height - 1);
                using (var path = RoundedPath(rect, 8))
                using (var pen = new Pen(focused ? Primary : BorderStrong, focused ? 2 : 1))
                {
                    e.Graphics.DrawPath(pen, path);
                }
            };

            shell.Controls.Add(textBox);
            return shell;
        }

        internal static Label CreateCaption(string text)
        {
            return new Label
            {
                Text = text,
                AutoSize = true,
                Font = Caption(),
                ForeColor = TextSecondary,
                BackColor = Surface
            };
        }

        // ---------- Nút ----------

        internal static void StylePrimaryButton(Button button)
        {
            button.FlatStyle = FlatStyle.Flat;
            button.FlatAppearance.BorderSize = 0;
            button.FlatAppearance.MouseOverBackColor = PrimaryHover;
            button.FlatAppearance.MouseDownBackColor = PrimaryPressed;
            button.BackColor = Primary;
            button.ForeColor = Color.White;
            button.Font = new Font(FontFamily, 10.5F, FontStyle.Bold);
            button.Cursor = Cursors.Hand;
            button.UseVisualStyleBackColor = false;

            ApplyRoundedRegion(button, 8);
            button.Resize += (sender, e) => ApplyRoundedRegion(button, 8);
            button.EnabledChanged += (sender, e) =>
            {
                button.BackColor = button.Enabled ? Primary : BorderStrong;
                button.Cursor = button.Enabled ? Cursors.Hand : Cursors.Default;
            };
        }

        /// <summary>
        /// Nút phụ: nền xám nhạt, không viền (tránh hiện tượng viền chữ nhật bị Region bo góc cắt mất 4 góc).
        /// </summary>
        internal static void StyleSecondaryButton(Button button)
        {
            button.FlatStyle = FlatStyle.Flat;
            button.FlatAppearance.BorderSize = 0;
            button.FlatAppearance.MouseOverBackColor = SecondaryHover;
            button.FlatAppearance.MouseDownBackColor = BorderStrong;
            button.BackColor = SecondarySurface;
            button.ForeColor = TextPrimary;
            button.Font = new Font(FontFamily, 10F, FontStyle.Regular);
            button.Cursor = Cursors.Hand;
            button.UseVisualStyleBackColor = false;

            ApplyRoundedRegion(button, 8);
            button.Resize += (sender, e) => ApplyRoundedRegion(button, 8);
        }
    }
}
