# Số Liệu Đo Đạc Định Lượng: Viết Thủ Công vs AI Hỗ Trợ

## 1. Thời Gian Thiết Kế & Lập Trình (Trung bình 3 lượt đo)
| Công việc | Thủ công (Manual) | AI hỗ trợ (ChatGPT-4 / Gemini) | Mức độ tối ưu |
|---|:---:|:---:|:---:|
| Thiết kế 12 test case BVA | 45 phút | 3 phút | **Nhanh hơn 93.3%** |
| Soạn thảo Page Object Classes (C#) | 35 phút | 6 phút | **Nhanh hơn 82.8%** |
| Viết kịch bản Data-driven Testing | 40 phút | 8 phút | **Nhanh hơn 80.0%** |
| Debug lỗi cú pháp & hiệu chỉnh locator | 10 phút | 12 phút (sửa AI code) | Chậm hơn 20% (overhead rà soát) |
| **Tổng thời gian hoàn tất** | **130 phút** | **29 phút** | **Tiết kiệm 77.7% thời gian** |

## 2. Đo Đạc Dòng Mã (Lines of Code - LOC)
| Thành phần | LOC thủ công | LOC do AI sinh ban đầu | LOC sau khi hiệu chỉnh | Tỷ lệ code tái sử dụng |
|---|:---:|:---:|:---:|:---:|
| LoginPage.cs | 42 | 48 | 45 | **93.7%** |
| CalculatorPage.cs | 56 | 62 | 58 | **93.5%** |
| Demo3_BvaTests.cs | 68 | 75 | 70 | **93.3%** |
| **Tổng cộng** | **166** | **185** | **173** | **93.5%** |

## 3. Kết Luận Thực Nghiệm
- AI giúp tăng tốc đáng kể khâu viết khung test (boilerplate code) và mở rộng bộ test case biên.
- Bắt buộc phải có kỹ sư SDET rà soát (Human-in-the-loop) để sửa các sai lệch về tên AutomationId (tnCalculate vs tnSum) và chuỗi kết quả mong đợi.
