def length_of_longest_substring(str, k):
  """
    HIGH LEVEL:
      This is another sliding window problem.
      The trick to these problems where they ask to find the longest substring AFTER REPLACEMENT, 
      is to keep track of the max repeating character.
      If the difference between the current substring and the max_repeating character is greater than k,
      then that means you have too many characters to replace, therefore update the sliding window.

      After every expansion of the right side of the window, update the max length.

      Time: O(n), n = len(str)
      Space: O(1), since in this case, we're only using the lowercase alphabet, if the string is the entire alphabet, then
      worst case its O(26) which can be simplified to O(1)
  
  """
  left, max_length, max_repeat = 0, float("-inf"),  float("-inf")
  freq = {}

  for right in range(len(str)):
    if str[right] not in freq:
      freq[str[right]] = 0
    freq[str[right]] += 1

    max_repeat = max(max_repeat, freq[str[right]])

    if len(str[left:right+1]) - max_repeat > k:
      freq[str[left]] -= 1
      left += 1
    
    max_length = max(max_length, len(str[left:right+1]))

  return max_length
