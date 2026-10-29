using System;
using System.Collections.Generic;
using System.IO;
using NPOI.SS.UserModel;
using NPOI.XSSF.UserModel;
using NUnit.Framework;

namespace MiniSumTests.Helpers
{
    public static class ExcelHelper
    {
        public static IEnumerable<TestCaseData> ReadBvaData(string filePath)
        {
            if (!File.Exists(filePath))
            {
                throw new FileNotFoundException($"Không tìm thấy file Excel dữ liệu kiểm thử tại: {filePath}");
            }

            using var file = new FileStream(filePath, FileMode.Open, FileAccess.Read);
            IWorkbook workbook = new XSSFWorkbook(file);
            ISheet sheet = workbook.GetSheetAt(0);

            // Duyệt từ dòng 1 (bỏ dòng tiêu đề row 0)
            for (int r = 1; r <= sheet.LastRowNum; r++)
            {
                IRow row = sheet.GetRow(r);
                if (row == null) continue;

                // Lấy ô A, ô B và kết quả mong muốn Expected Result
                string a = GetCellValue(row.GetCell(1));
                string b = GetCellValue(row.GetCell(2));
                string expected = GetCellValue(row.GetCell(3));

                if (string.IsNullOrWhiteSpace(a) && string.IsNullOrWhiteSpace(b))
                    continue;

                yield return new TestCaseData(a, b, expected)
                    .SetName($"BVA_Line_{r:D2}_({a}+{b}={expected})");
            }
        }

        private static string GetCellValue(ICell cell)
        {
            if (cell == null) return string.Empty;
            return cell.CellType switch
            {
                CellType.Numeric => cell.NumericCellValue.ToString(),
                CellType.String => cell.StringCellValue.Trim(),
                CellType.Boolean => cell.BooleanCellValue.ToString(),
                CellType.Formula => cell.ToString(),
                _ => cell.ToString()?.Trim() ?? string.Empty
            };
        }
    }
}