def find_substring(str, pattern):

  """
    HIGH LEVEL:
      Similar approach to permutation in a string problem, with one difference. The substring can have letters that aren't
      part of the pattern string, we're just looking for a substring not a permutation.

      Time: O(n + m), n = len(str), m = len(pattern)
      Space: O(m), m = len(pattern)

      Here's the high level overview:
      * variables:
        left, matched, substr_left = 0, 0, 0
        min_length = float("inf")
        freq = {}

      * Build a dictionary that keeps track of the frequencies of each character in the pattern

      *Iterate the string:
        keep a running count of every matching instance of a character in frequency dictionary.
        while matched count == len(pattern):
          * if current window is < min_length:
            * update min_length
            * update the start of the substr by assigning it to left pointer index
          
          * shrink the window
          * if char @left pointer is in freq:
            * decrement matched count if current freq count == 0
            * increment frequency count of char @left pointer

      if min_length was never updated:
        return empty string as there is no substring that has the pattern
      otherwise return substring[substr_left:substr_left+min_length]

  """
  
  freq = {}
  matched = 0
  left = 0
  substr_left = 0
  min_length = len(str) + 1

  # build hashmap of frequencies per letter in pattern
  for letter in pattern:
    if letter not in freq:
      freq[letter] = 0
    freq[letter] += 1

  # extend the window
  for right in range(len(str)):
    char = str[right]

    if char in freq:
      freq[char] -= 1
      if freq[char] >= 0:
        matched += 1
    
    while matched == len(pattern):
      if right - left + 1 < min_length:
        min_length = right - left + 1
        substr_left = left
      
      lchar = str[left]
      left += 1

      if lchar in freq:
        if freq[lchar] == 0:
          matched -= 1
        freq[lchar] += 1

  if min_length > len(str):
    return ""
      
  return str[substr_left:substr_left+min_length]