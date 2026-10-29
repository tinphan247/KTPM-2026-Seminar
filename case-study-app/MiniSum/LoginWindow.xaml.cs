using System.Windows;

namespace MiniSum
{
    public partial class LoginWindow : Window
    {
        // Tai khoan/mat khau hop le dung cho demo seminar
        private const string ValidUser = "abc";
        private const string ValidPass = "123";

        public LoginWindow()
        {
            InitializeComponent();
            txtUser.Focus();
        }

        private void BtnSubmit_Click(object sender, RoutedEventArgs e)
        {
            string user = txtUser.Text.Trim();
            string pass = txtPass.Password;

            if (string.IsNullOrEmpty(user) && string.IsNullOrEmpty(pass))
            {
                lblMessage.Text = "Vui long nhap tai khoan va mat khau";
                lblMessage.Foreground = System.Windows.Media.Brushes.DarkOrange;
                return;
            }
            if (string.IsNullOrEmpty(user))
            {
                lblMessage.Text = "Ten dang nhap khong duoc de trong";
                lblMessage.Foreground = System.Windows.Media.Brushes.DarkOrange;
                return;
            }
            if (string.IsNullOrEmpty(pass))
            {
                lblMessage.Text = "Mat khau khong duoc de trong";
                lblMessage.Foreground = System.Windows.Media.Brushes.DarkOrange;
                return;
            }

            if (user == ValidUser && pass == ValidPass)
            {
                lblMessage.Text = "Dang nhap thanh cong";
                lblMessage.Foreground = System.Windows.Media.Brushes.Green;

                // Mo cua so Calculator va dong cua so Login sau 1s de Test Runner (Katalon/WinAppDriver) doc duoc checkpoint lblMessage
                var main = new MainWindow();
                main.Show();
                Dispatcher.InvokeAsync(async () =>
                {
                    await System.Threading.Tasks.Task.Delay(1000);
                    this.Close();
                });
            }
            else
            {
                lblMessage.Text = "Sai tai khoan hoac mat khau";
                lblMessage.Foreground = System.Windows.Media.Brushes.Red;
                txtPass.Clear();
                txtUser.Focus();
                txtUser.SelectAll();
            }
        }
    }
}
