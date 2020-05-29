/*
Given two words word1 and word2, find the minimum number
of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
*/

using System;

namespace HandsOn.ConsoleApp
{
    public class MinimumEditDistance
    {
        public int MinDistance(string word1, string word2)
        {
            int[,] dp = new int[word1.Length + 1, word2.Length + 1];

            // initialize the dp table
            for (int i = 1; i <= word2.Length; i++)
            {
                // word to
                dp[0, i] = i;
            }

            for (int i = 1; i <= word1.Length; i++)
            {
                // word from
                dp[i, 0] = i;
            }

            int cost = 0;
            for (int i = 1; i <= word1.Length; i++)
            {
                for (int j = 1; j <= word2.Length; j++)
                {
                    // if two char's match, its a noop
                    // cost = 0
                    if (word1[i - 1] == word2[j - 1])
                        cost = 0;
                    else
                        cost = 1;
                    // if char's don't match, 3 possible ways
                    // insert char into x
                    // remove char from y
                    // replace last char in x with last char in y
                    dp[i, j] = Math.Min(dp[i, j - 1], Math.Min(dp[i - 1, j], dp[i - 1, j - 1])) + cost;
                }
            }

            return dp[word1.Length, word2.Length];
        }
    }
}