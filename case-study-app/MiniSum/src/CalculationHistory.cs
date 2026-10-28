using System.Collections.Generic;

namespace MiniSum
{
    /// <summary>
    /// Lịch sử tính toán trong bộ nhớ, chỉ dùng ở phiên bản v2.
    /// </summary>
    internal static class CalculationHistory
    {
        private static readonly List<string> Entries = new List<string>();

        internal static void Add(string entry)
        {
            Entries.Insert(0, entry);
        }

        internal static IReadOnlyList<string> Snapshot()
        {
            return Entries;
        }
    }
}
