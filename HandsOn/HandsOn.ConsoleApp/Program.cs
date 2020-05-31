using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace HandsOn.ConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            var inputString = "hit";
            var targetString = "cog";

            IList<String> list = new List<String> { "hot", "dot", "dog", "lot", "log", "cog" };

            int expectedValue = 5;

            var actual_value = new WordLadder().FindMinLadder(inputString, targetString, list);

            Trace.Assert(actual_value == expectedValue, $"Returned value - {actual_value}");

            list = new List<String> { "hot", "dot", "dog", "lot", "log" };

            expectedValue = 0;
            actual_value = new WordLadder().FindMinLadder(inputString, targetString, list);

            Trace.Assert(actual_value == expectedValue, $"Returned value - {actual_value}");

            list = new List<String> { "hot", "dog", "dot" };

            inputString = "hot";
            targetString = "dog";
            expectedValue = 3;

            actual_value = new WordLadder().FindMinLadder(inputString, targetString, list);

            Trace.Assert(actual_value == expectedValue, $"Returned value - {actual_value}");

            int size = 5;

            var uf = new UnionFind(size);

            System.Console.WriteLine("Total sets :" + uf.getTotalSet());

            uf.union(0, 1);
            Trace.Assert(uf.getSetSize(0) == 2);

            uf.union(1, 0);
            Trace.Assert(uf.getSetSize(0) == 2);
            Trace.Assert(uf.getTotalSet() == 4);

            uf.union(1, 2);
            Trace.Assert(uf.getSetSize(0) == 3);
            Trace.Assert(uf.getSetSize(3) == 1);
            Trace.Assert(uf.getTotalSet() == 3);

            uf = new UnionFind(12);

            IEnumerable<Edge> edges = new List<Edge>{
                new Edge(1, 2),
                new Edge(1, 7),
                new Edge(1, 8),
                new Edge(2, 3),
                new Edge(2, 6),
                new Edge(3, 4),
                new Edge(3, 5),
                new Edge(8, 9),
                new Edge(8, 12),
                new Edge(9, 10),
                new Edge(9, 11),
                new Edge(11, 12)
            };

            Graph g = new Graph(edges);
            uf = new UnionFind(g.Vertices.Count);

            Trace.Assert(uf.FindCycle(g) == true);

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
