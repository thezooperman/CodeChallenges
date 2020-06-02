from typing import List


class Solution:
    cache = dict()
    def helper(self, input: str, end: int, word_dict: set):
        result = set()

        if end <= 0:
            return ("",)

        if end in self.cache:
            return self.cache[end]

        start = 0
        while start < end:
            new_str = input[start: end]
            if new_str in word_dict:
                tmp_list = self.helper(input, start, word_dict)
                for char in tmp_list:
                    if len(char) == 0:
                        result.add(new_str)
                    else:
                        result.add(char + " " + new_str)
            start += 1

        self.cache[end] = result
        return list(result)

    def wordBreak(self, string: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        self.cache.clear()
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
    s = "catsanddog"
    word_dict = ["cat", "cats", "and", "sand", "dog"]
    expected_output = ["cat sand dog", "cats and dog"]

    print("String:{}".format(s))
    actual = obj.wordBreak(s, word_dict)
    assert actual.sort() == expected_output.sort(), print(actual)

    
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    word_dict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    expected_output = []

    print("String:{}".format(s))
    actual = obj.wordBreak(s, word_dict)
    assert actual == expected_output, print(actual)

    s = "pineapplepenapple"
    word_dict = ["apple", "pen", "applepen", "pine", "pineapple"]
    expected_output = ["pine apple pen apple", "pine applepen apple", "pineapple pen apple"]

    print("String:{}".format(s))
    actual = obj.wordBreak(s, word_dict)
    assert actual.sort() == expected_output.sort(), print(actual)

    s = "catsandog"
    word_dict = ["cat", "cats", "and", "sand", "dog"]
    expected_output = []

    print("String:{}".format(s))
    actual = obj.wordBreak(s, word_dict)
    assert actual == expected_output, print(actual)

