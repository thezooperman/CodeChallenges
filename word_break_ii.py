from typing import List


class Solution:
    cache = dict()

    # visited = set()

    def helper(self, input: str, end: int, word_dict: set):
        result = set()
        visited = set()
        if end <= 0:
            return ("",)

        if input in self.cache:
            return self.cache[input]

        start = 0
        while start < end:
            new_str = input[start: end]
            if new_str in word_dict and new_str not in visited:
                visited.add(new_str)
                tmp_list = self.helper(input, start, word_dict)
                for char in tmp_list:
                    if len(char) == 0:
                        result.add(new_str)
                    else:
                        result.add(char + " " + new_str)
            start += 1
            # if new_str in visited:
            #     visited.remove(new_str)
        self.cache[end] = result
        # print(visited)
        return list(result)

    def wordbreak(self, string: str, wordDict: List[str]) -> List[str]:
        self.cache.clear()
        # self.visited.clear()
        wordDict = set(wordDict)
        return self.helper(string, len(string), wordDict)

    # def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    # dp solution
    #     dp = defaultdict(list)
    #     dp[0] = [""]
    #     words = set(wordDict)
    #
    #     for i in range(1, len(s) + 1):
    #         for j in range(i):
    #             if not dp[j]:
    #                 continue
    #             sub_str = s[j:i]
    #             if sub_str in words:
    #                 dp[i].extend([c + " " + sub_str if c
    #                               else sub_str for c in
    #                               dp[j]])
    #
    #     return dp[len(s)]


if __name__ == "__main__":
    obj = Solution()
    # s = "catsanddog"
    # word_dict = ["cat", "cats", "and", "sand", "dog"]
    # expected_output = True

    # print(obj.wordBreak(s, word_dict))

    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # word_dict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    #
    # print(obj.wordBreak(s, word_dict))

    s = "pineapplepenapple"
    word_dict = ["apple", "pen", "applepen", "pine", "pineapple"]

    print(obj.wordbreak(s, word_dict))
