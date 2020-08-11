def find_permutation(str, pattern):
  
  """
    HIGH LEVEL:
      Create a hashmap that keeps track of frequency count of each letter in pattern.
      You want to use a sliding window technique, and keep expanding the window until you reach
      len(pattern), at that point you need to shrink the window

      In between the iterations, you need to see if the current letter that you're on is in the 
      hashmap. If it is, then reduce the freq count by 1. If by subtracting 1 from the freq count results 
      to 0, then this means that you have a matching piece of the permutation. The "match_count" will essentially
      keep track of how many of the letters we have matched thus far with the pattern. If at any point
      the match_count and len(freq) are EQUAL, return True because this means we have a permutation.

      if we have expanded the window and it's now greater than the pattern, we need to shrink it.
      By doing so, some processing is needed. First capture the letter of the left side of the window.
      update the left pointer (meaning shrinking it), check to see if the letter is in the hashmap.
      If it is, check if the freq count is 0, if it is, reduce match_count 
      increase freq count by 1.

      If you end up iterating the entire string without returning True. This means the string has no permutation
      of the pattern.
      return False

      Time: O(n), n = len(str)
      Space: O(m), m = len(pattern)
  """
  freq = {}
  match_count = 0
  left = 0

  for char in pattern:
    if char not in freq:
      freq[char] = 0
    freq[char] += 1

  for right in range(len(str)):
    letter = str[right]

    if letter in freq:
      freq[letter] -= 1
      if freq[letter] == 0:
        match_count += 1
    
    if match_count == len(freq):
      return True
    
    if right >= len(pattern) - 1:
      letter = str[left]
      left += 1
      if letter in freq:
        if freq[letter] == 0:
          match_count -= 1
        freq[letter] += 1

  return False
