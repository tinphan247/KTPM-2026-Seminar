# Sơ đồ vẽ lại cho báo cáo seminar

Thư mục này chứa **18 sơ đồ** được vẽ lại từ các khối ASCII-art và mã Mermaid nằm trong
`seminar-final.docx`. File Word **không bị sửa** — ảnh ở đây để chèn thủ công.

## Thông số kỹ thuật

| Thuộc tính | Giá trị |
|---|---|
| Bề rộng canvas | 1950 px |
| Độ phân giải ghi trong file | 300 dpi |
| Kích thước khi chèn | **6,5 in = 16,51 cm** (đúng vùng soạn thảo A4 với lề 0,98 + 0,79 in) |
| Định dạng | PNG, nền trắng, không có caption "Hình x.y" bên trong ảnh |
| Font | Segoe UI (thường/đậm), Consolas cho mã lệnh |

Chiều cao trong bảng dưới là chiều cao **tự động** khi kéo rộng ảnh về 6,5 in (Word giữ tỉ lệ).

## Cách chèn vào Word

1. Đặt con trỏ tại vị trí cần chèn (xem bảng ánh xạ).
2. **Insert → Pictures → This Device…** → chọn file PNG.
3. **Picture Format → Width = 6.5"** (16,51 cm), giữ nguyên *Lock Aspect Ratio*.
4. Căn giữa đoạn chứa ảnh; caption (nếu cần) đặt bên dưới bằng **References → Insert Caption**.

## Ánh xạ ảnh ↔ vị trí trong `seminar-final.docx`

Thứ tự dưới đây theo đúng thứ tự xuất hiện trong tài liệu.

| # | Tệp ảnh | Vị trí trong Word | Nội dung | Cao khi chèn | Caption trong Word |
|---|---|---|---|---|---|
| 1 | `01-phan-loai-desktop-application.png` | Ch.2 – §1.1 *Phân loại Desktop Application* | Cây phân loại desktop app (Win32, WinForms, WPF, UWP, Electron…) | 3,48 in | chưa có |
| 2 | `02-luong-checkpoint.png` | Ch.2 – §5.3 *Kiến trúc Assertion* | Luồng checkpoint: thao tác → lấy giá trị thực tế → so với oracle → PASS/FAIL | 3,52 in | chưa có |
| 3 | `03-so-sanh-pom.png` | Ch.2 – §6.1 *Khái niệm POM* | So sánh kiểm thử truyền thống và Page Object Model | 2,29 in | **Hình 2.5** |
| 4 | `04-luong-test-oracle.png` | Ch.2 – §9.1 *Khái niệm Test Oracle* | Luồng Test Oracle và các nguồn dữ liệu đối chiếu | 3,04 in | chưa có |
| 5 | `16-pipeline-tu-dong-hoan-toan.png` | Ch.2 – §11.1 *Fully Automated* | Đường ống CI/CD 6 khâu, tự động 100% | 1,54 in | chưa có |
| 6 | `17-quy-trinh-ban-tu-dong.png` | Ch.2 – §11.2 *Semi-Automated* | Quy trình bán tự động: tự động → thủ công → tự động | 2,79 in | chưa có |
| 7 | `18-bang-quyet-dinh-automation.png` | Ch.2 – §13 *Khi nào nên dùng Automation Testing?* | Bảng quyết định NÊN / KHÔNG NÊN + quy tắc "lặp lại ≥ 3 lần" | 2,57 in | chưa có |
| 8 | `05-bo-tieu-chi-6-nhom.png` | Ch.3 – §1.1 *Sơ đồ cấu trúc 6 nhóm tiêu chí* | Sáu nhóm tiêu chí đánh giá công cụ desktop automation | 2,94 in | chưa có |
| 9 | `06-sequence-kien-truc-thi-hanh.png` | Ch.4 – §2.1.1 *Sơ đồ kiến trúc phân tầng* | Sequence diagram 5 lifeline: Kịch bản → Katalon Engine → WinAppDriver → UIA → AUT | 8,40 in | chưa có |
| 10 | `07-quy-trinh-object-spy.png` | Ch.4 – §2.3.2 *Quy trình từng bước dùng Windows Object Spy* | 6 bước: khởi động driver → mở Spy → cấu hình AUT → bắt phần tử → verify → lưu Object Repository | 1,82 in | chưa có |
| 11 | `08-cau-truc-du-an-katalon.png` | Ch.4 – §2.4.1 *Mô hình phân cấp kiểm thử* | TSC → Test Suite → Test Case → Object Repository, kèm Test Data và Test Listener | 2,81 in | chưa có |
| 12 | `09-demo-katalon-ba-buoc.png` | Ch.4 – §5 *Định hướng kịch bản Demo* | Roadmap 3 demo Katalon Studio (thiết lập → cơ bản → nâng cao) | 0,93 in | chưa có |
| 13 | `10-kien-truc-bon-tang-winappdriver.png` | Ch.5 – §2.1 *Kiến trúc thực thi* | 4 tầng: Test Script → WinAppDriver.exe → UIA → AUT | 2,87 in | chưa có |
| 14 | `11-demo-winappdriver-ba-buoc.png` | Ch.5 – §4 *Định hướng kịch bản Demo* | Roadmap 3 demo WinAppDriver thuần (thiết lập → cơ bản → nâng cao) | 0,93 in | chưa có |
| 15 | `12-gantt-so-sanh-thoi-gian.png` | Ch.6 – §4.3 *Biểu đồ trực quan hoá so sánh thời gian* | Gantt so sánh 120 / 90 / 29 phút cho cùng 12 ca BVA trên MiniSum | 3,18 in | chưa có |
| 16 | `13-so-do-chon-giai-phap.png` | Ch.6 – §6 *Ma trận lựa chọn giải pháp* | Bàn cân 3 lựa chọn: Katalon Studio / WinAppDriver thuần / WinAppDriver + AI | 1,89 in | chưa có |
| 17 | `14-nam-huong-ung-dung-ai.png` | Ch.7 – §2 *Năm hướng ứng dụng AI* | 5 hướng AI trọng tâm trong desktop automation | 2,28 in | **Hình 7.1** |
| 18 | `15-chuoi-thuc-nghiem-ai.png` | Ch.7 – §4 *Kết quả thực nghiệm* | Chuỗi thực nghiệm: AI Demo 1 (sinh test case BVA) → AI Demo 2 (sinh script C# + xác minh) | 2,21 in | **Hình 7.2** |

Ba vị trí đã có caption số trong Word (**Hình 2.5**, **Hình 7.1**, **Hình 7.2**) nên thay ảnh
đúng tại chỗ và giữ nguyên caption. Các vị trí còn lại hiện không có caption; nếu muốn bổ sung
thì đánh số tiếp theo thứ tự hình trong từng chương.

## Hai chỗ đã chuẩn hoá khi vẽ lại

1. **`07-quy-trinh-object-spy.png`** – bản ASCII trong Word đánh số bước bị nhảy (1, 2, 3, 5, 6, 7)
   trong khi phần văn xuôi §2.3.2 mô tả đúng **6 bước**. Ảnh vẽ lại đánh số 1–6 theo văn xuôi.
2. **`08-cau-truc-du-an-katalon.png`** – bản Mermaid dùng 3 mũi tên nét đứt chồng chéo để chỉ
   Test Listener. Ảnh vẽ lại thể hiện Test Listener bằng **khung nét đứt bao quanh** Test Suite
   và Test Case, kèm chú thích cơ chế hook `@Before / @After / Auto Screenshot`.

## Cấu trúc thư mục

```
docs/diagrams/
├── 01..18-*.png        # 18 ảnh đã render, sẵn sàng chèn Word
├── README.md           # file này
└── src/
    ├── svgkit.py       # toolkit SVG → PNG (measure text, wrap, box, arrow, render Chrome)
    ├── build1.py       # sơ đồ 01–05
    ├── build2.py       # sơ đồ 06–11
    ├── build3.py       # sơ đồ 12–15
    └── build4.py       # sơ đồ 16–18
```

## Sinh lại ảnh (tuỳ chọn)

Yêu cầu: Python 3 + `Pillow`, Google Chrome (đường dẫn Chrome khai báo ở đầu `src/svgkit.py`).

```powershell
cd docs/diagrams/src
python build1.py
python build2.py
python build3.py
python build4.py
```

Ảnh được ghi vào `src/out/`, sau đó chép đè lên thư mục cha. Mọi kích thước, màu, font và nội
dung chữ đều nằm trong các file `build*.py` nên có thể sửa nhanh nếu cần đổi câu chữ.
