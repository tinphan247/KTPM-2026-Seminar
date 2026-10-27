using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace MiniSum
{
    /// <summary>
    /// Màn hình Lịch sử tính toán (chỉ có ở phiên bản v2).
    /// AutomationId: winHistory, lstHistory, btnClose.
    ///
    /// Giao diện theo phong cách Fluent Light (xem Theme.cs).
    /// ListBox được vẽ lại từng dòng (OwnerDrawFixed) nhưng vẫn là control ListBox chuẩn,
    /// nên automation vẫn đọc được AutomationId, ControlType và nội dung từng dòng.
    /// </summary>
    public class HistoryForm : Form
    {
        public HistoryForm()
        {
            Name = "winHistory";
            Text = "MiniSum - Lich su tinh toan";
            ClientSize = new Size(440, 420);
            StartPosition = FormStartPosition.CenterParent;
            FormBorderStyle = FormBorderStyle.FixedDialog;
            MaximizeBox = false;
            MinimizeBox = false;
            Font = Theme.Body();
            BackColor = Theme.Canvas;
            DoubleBuffered = true;

            var accent = Theme.CreateAccentStrip(ClientSize.Width);

            var lblTitle = new Label
            {
                Name = "lblTitle",
                Text = "Lịch sử tính toán",
                AutoSize = true,
                Font = Theme.Title(18F),
                ForeColor = Theme.TextPrimary,
                BackColor = Theme.Canvas,
                Location = new Point(32, 24)
            };

            var lblSubtitle = new Label
            {
                Name = "lblSubtitle",
                Text = "Các phép tính đã thực hiện trong phiên làm việc này",
                AutoSize = true,
                Font = Theme.Body(9.5F),
                ForeColor = Theme.TextSecondary,
                BackColor = Theme.Canvas,
                Location = new Point(34, 64)
            };

            var listShell = Theme.CreateTintedPanel(Theme.Surface, Theme.Border, 10);
            listShell.Location = new Point(24, 96);
            listShell.Size = new Size(392, 236);

            var lstHistory = new ListBox
            {
                Name = "lstHistory",
                Location = new Point(10, 10),
                Size = new Size(372, 216),
                Font = Theme.Body(10F),
                BackColor = Theme.Surface,
                ForeColor = Theme.TextPrimary,
                BorderStyle = BorderStyle.None,
                IntegralHeight = false,
                DrawMode = DrawMode.OwnerDrawFixed,
                ItemHeight = 32,
                TabIndex = 0
            };
            lstHistory.DrawItem += LstHistory_DrawItem;

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

            listShell.Controls.Add(lstHistory);

            var btnClose = new Button
            {
                Name = "btnClose",
                Text = "DONG",
                Location = new Point(316, 352),
                Size = new Size(100, 40),
                TabIndex = 1
            };
            Theme.StyleSecondaryButton(btnClose);
            btnClose.Click += (sender, e) => Close();

            CancelButton = btnClose;
            Controls.Add(accent);
            Controls.Add(lblTitle);
            Controls.Add(lblSubtitle);
            Controls.Add(listShell);
            Controls.Add(btnClose);
        }

        private void LstHistory_DrawItem(object sender, DrawItemEventArgs e)
        {
            if (e.Index < 0)
            {
                return;
            }

            var listBox = (ListBox)sender;
            bool selected = (e.State & DrawItemState.Selected) == DrawItemState.Selected;
            Rectangle bounds = e.Bounds;

            using (var background = new SolidBrush(selected ? Theme.Primary : Theme.Surface))
            {
                e.Graphics.FillRectangle(background, bounds);
            }

            if (!selected)
            {
                using (var line = new Pen(Theme.Border))
                {
                    e.Graphics.DrawLine(line, bounds.Left + 10, bounds.Bottom - 1, bounds.Right - 10, bounds.Bottom - 1);
                }
            }

            string text = listBox.Items[e.Index] as string ?? string.Empty;
            var textBounds = new Rectangle(bounds.Left + 12, bounds.Top, bounds.Width - 24, bounds.Height);

            TextRenderer.DrawText(
                e.Graphics,
                text,
                listBox.Font,
                textBounds,
                selected ? Color.White : Theme.TextPrimary,
                TextFormatFlags.Left | TextFormatFlags.VerticalCenter | TextFormatFlags.EndEllipsis);
        }
    }
}
