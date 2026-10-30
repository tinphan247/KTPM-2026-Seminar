# Ket Qua Sinh Test Case BVA Tu Gemini Advanced

Dưới đây là 12 ca kiểm thử BVA do Gemini Advanced sinh ra:

| STT | TC ID | Input A | Input B | Expected Display | Status |
|:---:|---|:---:|:---:|---|:---:|
| 1 | BVA_01 | -99 | 0 | Ket qua: -99 + 0 = -99 | Pass |
| 2 | BVA_02 | -98 | 0 | Ket qua: -98 + 0 = -98 | Pass |
| 3 | BVA_03 | 0 | 0 | Ket qua: 0 + 0 = 0 | Pass |
| 4 | BVA_04 | 98 | 0 | Ket qua: 98 + 0 = 98 | Pass |
| 5 | BVA_05 | 99 | 0 | Ket qua: 99 + 0 = 99 | Pass |
| 6 | BVA_06 | 0 | -99 | Ket qua: 0 + -99 = -99 | Pass |
| 7 | BVA_07 | 0 | -98 | Ket qua: 0 + -98 = -98 | Pass |
| 8 | BVA_08 | 0 | 98 | Ket qua: 0 + 98 = 98 | Pass |
| 9 | BVA_09 | 0 | 99 | Ket qua: 0 + 99 = 99 | Pass |
| 10 | BVA_10 | -100 | 0 | A ngoai mien [-99, 99] | Error Handled |
| 11 | BVA_11 | 0 | 100 | B ngoai mien [-99, 99] | Error Handled |
| 12 | BVA_12 | 100 | 100 | A ngoai mien [-99, 99] | Error Handled |
