using System.Windows;

namespace MiniSum
{
    public partial class MainWindow : Window
    {
        // Gioi han theo yeu cau: A, B in [-99, 99]
        private const int LowerBound = -99;
        private const int UpperBound = 99;

        public MainWindow()
        {
            InitializeComponent();
            txtA.Focus();
        }

        private void BtnSum_Click(object sender, RoutedEventArgs e)
        {
            string aRaw = txtA.Text.Trim();
            string bRaw = txtB.Text.Trim();

            // Xoa ket qua cu
            lblResult.Text = "";
            lblError.Text = "";

            if (string.IsNullOrEmpty(aRaw) || string.IsNullOrEmpty(bRaw))
            {
                lblError.Text = "Vui long nhap day du gia tri A va B";
                return;
            }

            // Kiem tra kieu du lieu
            if (!int.TryParse(aRaw, out int a) || !int.TryParse(bRaw, out int b))
            {
                lblError.Text = "Gia tri khong hop le: phai la so nguyen";
                return;
            }

            // Kiem tra bien (BVA)
            if (a < LowerBound || a > UpperBound)
            {
                lblError.Text = $"A ngoai mien [{LowerBound}, {UpperBound}]";
                return;
            }
            if (b < LowerBound || b > UpperBound)
            {
                lblError.Text = $"B ngoai mien [{LowerBound}, {UpperBound}]";
                return;
            }

            // Tinh toan
            int result = a + b;
            lblResult.Text = $"Ket qua: {a} + {b} = {result}";
        }

        private void BtnLogout_Click(object sender, RoutedEventArgs e)
        {
            var login = new LoginWindow();
            login.Show();
            this.Close();
        }
    }
}
