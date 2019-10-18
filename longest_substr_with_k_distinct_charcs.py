def longest_substring_with_k_distinct(str, k):
  # TODO: Write your code here
  char_freq = {}
  cur_win = max_win = 0

  #loop over
  for c in str:
    if c not in char_freq:
      char_freq[c] = 1
    if len(char_freq) <= k:
      cur_win += 1
      max_win = max(cur_win, max_win)
    else:
      cur_win = 0
      char_freq.clear()
  return max_win

def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("aabbcc", 3)))


main()
