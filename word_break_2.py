from typing import List


class Solution:
    cache = dict()
    result = []

    def helper(self, string: str, word_dict: set) -> None:
        if len(string) == 0:
            print(self.result)
            return True

        if string in self.cache:
            return self.cache[string]

        for i in range(1, len(string) + 1):
            new_word = string[:i]
            if new_word in word_dict and self.helper(string[i:], word_dict):
                self.result.append(new_word)
                print(self.result)
                self.cache[string] = True
                return True

        self.cache[string] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = {_ for _ in wordDict}
        self.result.clear()
        self.helper(s, word_set)
        return self.result


if __name__ == "__main__":
    obj = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    # expected_output = True

    # assert expected_output == obj.wordBreak(s, word_dict)
    print(obj.wordBreak(s, wordDict))
