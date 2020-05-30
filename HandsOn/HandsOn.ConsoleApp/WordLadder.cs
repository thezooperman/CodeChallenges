using System;
using System.Text;
using System.Collections.Generic;
using System.Linq;

namespace HandsOn.ConsoleApp
{
    public class WordLadder
    {
        public int LadderLength(String beginWord, String endWord, IList<String> wordList)
        {
            int n = beginWord.Length;

            ISet<string> dic = wordList.ToHashSet();
            ISet<string> visited = new HashSet<string>();
            Queue<string> bfs = new Queue<string>();
            bfs.Enqueue(beginWord);
            visited.Add(beginWord);
            int pathLength = 0;

            while (bfs.Count > 0)
            {
                int count = bfs.Count;
                for (int i = 0; i < count; i++)
                {
                    var current = bfs.Dequeue();
                    if (current == endWord)
                    {
                        pathLength++;
                        return pathLength;
                    }

                    StringBuilder sb = new StringBuilder(current);
                    for (int j = 0; j < n; j++)
                    {
                        var oldChar = sb[j];
                        for (char k = 'a'; k <= 'z'; k++)
                        {
                            sb[j] = k;
                            var newWord = sb.ToString();

                            if (!visited.Contains(newWord) && dic.Contains(newWord))
                            {
                                bfs.Enqueue(newWord);
                                visited.Add(newWord);
                            }
                        }
                        sb[j] = oldChar;
                    }
                }
                pathLength++;
            }
            return 0;
        }
    

        public int FindMinLadder(String start, String end, IList<String> list)
        {
            ISet<String> wordList = new HashSet<String>(list);

            if (!wordList.Contains(end))
                return 0;
            
            var queue = new Queue<Tuple<String, Int32>>();
            var visited = new HashSet<String>();

            queue.Enqueue(Tuple.Create(start, 1));

            while (queue.Count > 0)
            {
                (String word, int step) = queue.Dequeue();

                if (word.Equals(end, StringComparison.InvariantCultureIgnoreCase))
                    return step;
                

                for (int i = 0; i < word.Length; i++)
                {
                    for (char c = 'a'; c <= 'z'; c++)
                    {
                        var new_word = word.Substring(0, i) + c + word.Substring(i + 1, word.Length - i - 1);

                        if (wordList.Contains(new_word) && !visited.Contains(new_word)){
                            queue.Enqueue(Tuple.Create(new_word, step + 1));
                            visited.Add(new_word);
                            wordList.Remove(new_word);
                        }
                    }    
                }
            }

            return 0;
        }
    }
}