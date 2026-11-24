# Thư Mục Tài Nguyên Thực Nghiệm AI (AI Test Automation Repository)
## Chuyên Đề: Automation Testing Cho Desktop Applications

- **Thành viên phụ trách:** Trần Vũ Quang (MSSV: 23120346) - Nhóm 02
- **Mục tiêu:** Lưu trữ toàn bộ các mẫu Prompt kỹ thuật cao (Prompt Engineering), các phản hồi thô và phản hồi tinh chỉnh từ các mô hình ngôn ngữ lớn (OpenAI ChatGPT-4, Google Gemini 1.5 Pro, Anthropic Claude 3.5 Sonnet), cùng kịch bản mã nguồn C# NUnit WinAppDriver đã được debug và kiểm chứng trên môi trường thực tế.

---

## 📁 Cấu Trúc Thư Mục `ai/`

```text
ai/
├── README.md                                 # Tài liệu chỉ mục & hướng dẫn tổng quan (File này)
├── prompts/                                  # Chứa các tài liệu đặc tả & kỹ nghệ prompt
│   ├── minisum-spec.md                       # Đặc tả chi tiết ứng dụng MiniSum (UIA, rules, bounds)
│   ├── testcase-bva-prompt.md                # Kỹ thuật Prompt Zero-shot & Few-shot sinh ca BVA
│   └── script-gen-prompt.md                  # Kỹ thuật Prompt sinh mã C# NUnit WinAppDriver theo POM
└── output/                                   # Chứa kết quả sinh tự động, đánh giá & mã nguồn
    ├── chatgpt-bva-output.md                 # AI Demo 1a: Kết quả ChatGPT-4 & tinh chỉnh đa vòng
    ├── gemini-bva-output.md                  # AI Demo 1b: Đối chiếu kết quả Gemini 1.5 Pro & Claude 3.5
    ├── bva-evaluation.md                     # Đánh giá chất lượng: độ phủ biên, lỗi logic, ảo giác
    ├── bva-testcases.xlsx                    # File Excel 12 test case BVA chuẩn hóa cho toàn nhóm
    ├── chatgpt-script-output.cs              # AI Demo 2a: Mã C# NUnit ban đầu do ChatGPT-4 sinh
    ├── ai-script-debug-and-verification.md   # AI Demo 2b: Nhật ký debug 4 lỗi hệ điều hành và timing
    └── verified-script-output.cs             # Mã nguồn C# NUnit hoàn thiện đã chạy PASS 100%
```

---

## 📊 Tóm Tắt Kết Quả Định Lượng
- **Thời gian hoàn thành:** Giảm từ 120 phút (thủ công) xuống còn **29 phút** (giảm ~75%).
- **Tỷ lệ tái sử dụng mã AI:** Đạt **84.6%** (182/215 dòng mã giữ nguyên).
- **Độ chính xác BVA:** Đạt **100%** độ bao phủ biên sau khi áp dụng kỹ thuật Few-shot.
