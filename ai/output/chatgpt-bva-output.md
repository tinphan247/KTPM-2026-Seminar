# Ket Qua Sinh Test Case BVA Tu ChatGPT-4

Dưới đây là 12 ca kiểm thử phân tích giá trị biên (BVA) do ChatGPT-4 sinh ra từ đặc tả MiniSum:

| Test Case ID | Mô tả kịch bản | Giá trị A | Giá trị B | Kết quả mong đợi (Expected Result) | Loại test |
|---|---|:---:|:---:|---|:---:|
| **TC_BVA_01** | Hai biên nhỏ nhất hợp lệ | -99 | -99 | Ket qua: -99 + -99 = -198 | Valid |
| **TC_BVA_02** | Hai biên lớn nhất hợp lệ | 99 | 99 | Ket qua: 99 + 99 = 198 | Valid |
| **TC_BVA_03** | Điểm danh định (Zero) | 0 | 0 | Ket qua: 0 + 0 = 0 | Valid |
| **TC_BVA_04** | A biên dưới, B danh định | -99 | 0 | Ket qua: -99 + 0 = -99 | Valid |
| **TC_BVA_05** | A danh định, B biên dưới | 0 | -99 | Ket qua: 0 + -99 = -99 | Valid |
| **TC_BVA_06** | A biên trên, B danh định | 99 | 0 | Ket qua: 99 + 0 = 99 | Valid |
| **TC_BVA_07** | A danh định, B biên trên | 0 | 99 | Ket qua: 0 + 99 = 99 | Valid |
| **TC_BVA_08** | Lân cận biên dưới (Min+1) | -98 | -98 | Ket qua: -98 + -98 = -196 | Valid |
| **TC_BVA_09** | Lân cận biên trên (Max-1) | 98 | 98 | Ket qua: 98 + 98 = 196 | Valid |
| **TC_BVA_10** | A vượt biên dưới (Min-1) | -100 | 0 | A ngoai mien [-99, 99] | Invalid |
| **TC_BVA_11** | B vượt biên trên (Max+1) | 0 | 100 | B ngoai mien [-99, 99] | Invalid |
| **TC_BVA_12** | Cả A và B đều vượt biên trên | 100 | 100 | A ngoai mien [-99, 99] | Invalid |
