using System;
using System.Diagnostics;

namespace HandsOn.ConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            var obj = new Solution();

            int[] A = new int[] { 1, 4, 2 };
            int[] B = new int[] { 1, 2, 4 };

            int expectedOutput = 2;
            int actualOutput = obj.MaxUncrossedLines(A, B);

            Trace.Assert(actualOutput == expectedOutput);

            var mde = new MinimumEditDistance();
            var word_from = "horse";
            var word_to = "ros";

            expectedOutput = 3;
            actualOutput = mde.MinDistance(word_from, word_to);

            Trace.Assert(expectedOutput == actualOutput);

            String X = "ABCBDAB";
            String Y = "BDCABA";
            var lcs = new LCS();

            expectedOutput = 4;
            actualOutput = lcs.LongestCommonSubsequence(X, Y);

            Trace.Assert(actualOutput == expectedOutput);
        }
    }
}
