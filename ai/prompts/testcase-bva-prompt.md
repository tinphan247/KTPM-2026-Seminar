# Prompt: Sinh Bộ Ca Kiểm Thử Giá Trị Biên (BVA) Cho Desktop App

## System Prompt
Bạn là một kỹ sư Kiểm thử Phần mềm (SDET) chuyên sâu về lý thuyết thiết kế ca kiểm thử hộp đen (Black-box Testing) và tự động hóa ứng dụng desktop Windows.

## User Prompt (Few-shot Prompting)
Hãy thiết kế bộ ca kiểm thử theo kỹ thuật **Phân tích giá trị biên (Boundary Value Analysis - BVA)** cho hàm tính tổng hai số nguyên , B$ trên ứng dụng desktop MiniSum với các ràng buộc sau:
- Miền giá trị hợp lệ: , B \in [-99, 99]$.
- Các giá trị biên cần xét cho mỗi biến:
  - Giá trị nhỏ nhất trừ 1 (Invalid): -100
  - Giá trị nhỏ nhất (Valid min): -99
  - Giá trị nhỏ nhất cộng 1 (Valid min+): -98
  - Giá trị danh định / thông thường (Nominal): 0
  - Giá trị lớn nhất trừ 1 (Valid max-): 98
  - Giá trị lớn nhất (Valid max): 99
  - Giá trị lớn nhất cộng 1 (Invalid): 100
- Hãy sinh ra đúng **12 ca kiểm thử trọng tâm** (gồm kiểm thử biên hợp lệ và không hợp lệ), xuất dưới định dạng bảng Markdown có các cột: Test Case ID, Mô tả, Giá trị A, Giá trị B, Kết quả mong đợi (Expected Result), Loại kiểm thử (Valid/Invalid).
