# Automation Testing for Desktop Applications
## Phần 1: Introduction

> **Seminar – Phụ trách:** Tín  
> **Nội dung:** Bối cảnh · Lý do chọn đề tài · Mục tiêu seminar · Phạm vi kiểm thử  
> **Cập nhật lần cuối:** 02/10/2026  
> **Trạng thái:** Hoàn thành  

---

## 1. Bối cảnh

Phần mềm desktop vẫn chiếm vai trò đặc biệt quan trọng trong nhiều lĩnh vực: tài chính, ngân hàng, y tế, sản xuất công nghiệp, thiết kế đồ họa, kỹ thuật và quản trị nội bộ doanh nghiệp. Không giống như các ứng dụng web chạy trên nền trình duyệt, desktop app được cài đặt và vận hành trực tiếp trên hệ điều hành máy tính, tương tác sâu với tài nguyên phần cứng (file system, registry, drivers, thiết bị ngoại vi, GPU…) và đòi hỏi tiêu chuẩn rất cao về tính ổn định, độ bảo mật và hiệu năng.

Trong kỷ nguyên phát triển phần mềm theo các mô hình Agile/DevOps và CI/CD, chu kỳ phát hành phần mềm bị rút ngắn đáng kể. Các phương pháp kiểm thử thủ công (manual testing) thuần túy không còn đáp ứng kịp thời về tốc độ phản hồi lẫn độ phủ thử nghiệm, dễ dẫn đến hiện tượng trôi bug hoặc chậm tiến độ. Do đó, **Automation Testing** (Kiểm thử tự động) cho desktop applications trở thành một giải pháp tất yếu nhằm nâng cao chất lượng phần mềm và tối ưu chi phí kiểm thử dài hạn.

---

## 2. Lý do chọn đề tài

| Vấn đề thực tiễn | Lý do quan tâm nghiên cứu |
|---|---|
| **Vị trí của desktop app trong doanh nghiệp** | Nhiều hệ thống cốt lõi vẫn chạy trên desktop (ERP, SCADA, POS, ứng dụng xử lý dữ liệu nặng), nhu cầu kiểm thử chất lượng không suy giảm. |
| **Chi phí và hạn chế của kiểm thử thủ công** | Kiểm thử hồi quy bằng tay qua nhiều phiên bản tốn rất nhiều thời gian, công sức và dễ phát sinh sai sót do thao tác lặp lại. |
| **Độ phức tạp đặc thù của kiểm thử desktop** | Khác với web vốn chuẩn hóa theo DOM và HTML, desktop app phân mảnh sâu sắc theo framework UI (Win32, WPF, WinForms, Qt, Electron), đòi hỏi công cụ và kỹ thuật định danh chuyên biệt. |
| **Thách thức trong việc lựa chọn công cụ** | Hệ sinh thái công cụ automation desktop rất đa dạng (mã nguồn mở, thương mại, GUI-based, code-based), đội ngũ kiểm thử cần bộ tiêu chí rõ ràng để chọn đúng giải pháp. |
| **Xu hướng ứng dụng trí tuệ nhân tạo (AI)** | Các công nghệ GenAI và Computer Vision đang định hình lại cách sinh kịch bản kiểm thử, tự phục hồi selector (self-healing) và phân tích log lỗi. |

<p class="table-caption"><b>Bảng 1.1:</b> <i>Lý do lựa chọn và tính cấp thiết của đề tài kiểm thử tự động ứng dụng Desktop</i></p>


---

## 3. Mục tiêu seminar

Chuyên đề Seminar tập trung vào 5 mục tiêu cốt lõi sau:

1. **Làm chủ lý thuyết nền tảng:** Nắm vững các khái niệm, cơ chế điều khiển và kiến trúc của Automation Testing dành riêng cho môi trường Desktop Applications trên hệ điều hành Windows.
2. **Khảo sát thị trường và thiết lập tiêu chí chuẩn:** Xây dựng bộ khung 10 tiêu chí đánh giá toàn diện nhằm so sánh khách quan giữa hai trường phái công cụ: Low-Code GUI (Katalon Studio) và Code-First SDK (Microsoft WinAppDriver).
3. **Xây dựng kịch bản thực nghiệm và demo thực tế:** Triển khai 3 cấp độ demo trên cùng ứng dụng mẫu MiniSum (Cài đặt môi trường, Record & Playback kết hợp Checkpoint, và Data-Driven Testing với kỹ thuật phân tích giá trị biên BVA).
4. **Nghiên cứu ứng dụng Trí tuệ Nhân tạo (AI):** Khai thác Prompt Engineering 2 pha để tự động hóa thiết kế test case biên và sinh mã nguồn C# NUnit Page Object Model hoàn chỉnh.
5. **Thiết kế bài tập thực hành ứng dụng:** Xây dựng bài lab cá nhân 30 phút trực quan, độc lập, thao tác trực tiếp trên mã nguồn clone từ GitHub.

---

## 4. Phạm vi seminar

- **Hệ điều hành mục tiêu:** Môi trường Microsoft Windows (chiếm đa số các ứng dụng desktop doanh nghiệp).
- **Công nghệ ứng dụng thử nghiệm:** Ứng dụng xây dựng trên các nền tảng phổ biến như WinForms, WPF, Win32 hoặc Electron.
- **Kỹ thuật kiểm thử trọng tâm:**
  - Record & Playback (Ghi nhận và phát lại hành vi thao tác)
  - Data-Driven Testing (Kiểm thử điều khiển bằng dữ liệu)
  - Checkpoints & Assertions (Điểm kiểm tra trạng thái và dữ liệu)
  - Quản lý và xử lý đồng bộ hóa giao diện (Synchronization & Waits)
- **Mức độ nội dung:** Kết hợp từ cơ sở lý thuyết chuẩn mực đến thực hành triển khai mã nguồn demo và bài tập cụ thể.
