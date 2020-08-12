/*
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

 

Constraints:

    1 <= text1.length <= 1000
    1 <= text2.length <= 1000
    The input strings consist of lowercase English characters only.
*/

using System;
using System.Collections.Generic;
using System.Linq;

namespace HandsOn.ConsoleApp
{
    public class LCS
    {
        public int LongestCommonSubsequence(string text1, string text2)
        {
            int[,] dp = new int[text1.Length + 1, text2.Length + 1];

            for (int i = 1; i <= text1.Length; i++)
            {
                for (int j = 1; j <= text2.Length; j++)
                {
                    // if characters match, remove last characters
                    // from both text and check until end
                    // add 1 to result
                    if (text1[i - 1] == text2[j - 1])
                    {
                        dp[i, j] = dp[i - 1, j - 1] + 1;
                    }
                    else
                    {
                        // for no match, remove last character from text1 and check,
                        // ,remove last character from text2 and check,
                        // pick one with max value
                        dp[i, j] = Math.Max(dp[i - 1, j], dp[i, j - 1]);
                    }
                }
            }
            return dp[text1.Length, text2.Length];
        }

        private ICollection<String> LookupHelper(int[,] dp, String x, int m, String y, int n)
        {
            if (m == 0 || n == 0)
                return new List<String>();

            if (x[m - 1] == y[n - 1])
            {
                var lcs = this.LookupHelper(dp, x, m - 1, y, n - 1);

                foreach (var item in lcs)
                {
                    lcs.Add(item);
                }
            }

            return new List<String>();
        }

        private ICollection<String> LookUpLCS(int[,] dp, string x, string y)
        {
            return this.LookupHelper(dp, x, x.Length, y, y.Length);
        }

        public HashSet<String> AllLCS(string text1, string text2)
        {
            int[,] dp = new int[text1.Length + 1, text2.Length + 1];

            for (int i = 1; i <= text1.Length; i++)
            {
                for (int j = 1; j <= text2.Length; j++)
                {
                    // if characters match, remove last characters
                    // from both text and check until end
                    // add 1 to result
                    if (text1[i - 1] == text2[j - 1])
                    {
                        dp[i, j] = dp[i - 1, j - 1] + 1;
                    }
                    else
                    {
                        // for no match, remove last character from text1 and check,
                        // ,remove last character from text2 and check,
                        // pick one with max value
                        dp[i, j] = Math.Max(dp[i - 1, j], dp[i, j - 1]);
                    }
                }
            }
            return new HashSet<string>(this.LookUpLCS(dp, text1, text2));
        }
    }
}