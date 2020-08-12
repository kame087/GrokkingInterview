def find_string_anagrams(str, pattern):

  """
    HIGH LEVEL:
      An anagram is simply a permutation of the pattern. 
      * One way of tracking this is to create a hashmap that holds the frequencies of each char in the pattern.

      
      * Keep expanding until you have a window thats larger than the pattern length.
      * Iterate through the string:
        * at each iteration, check to see if current char is in the hashmap
          * if it is: deduct the frequency count of that char by 1
          * if that subtraction results to a frequency count of 0, this means you have completed a piece of the pattern
          * increment matched by 1
          
        * if matched == len(freq), then you have an anagram:
          * add left to the result list.
        
        * if len(window[left:right]) >= len(pattern):
          * you need to shrink the window
          * if char at left pointer is in the hashmap:
            * freq[char] == 0:
              * you need to deduct matched by 1
            * add frequency count back by 1.
          * shrink window by increasing left pointer.

      return result list

    Time: O(n+m), n = len(string), m = len(pattern)
    Space: O(m), m = len(pattern)
      
  
  """

  result_indices = []
  freq = {}
  matched = 0

  # build the freq of the pattern input
  for letter in pattern:
    if letter not in freq:
      freq[letter] = 0
    freq[letter] += 1

  left = 0
  for right in range(len(str)):
    char = str[right]
    if char in freq:
      freq[char] -= 1
      if freq[char] == 0:
        matched += 1

    # this is to check if you have a valid anagram
    if matched == len(freq):
      result_indices.append(left)

    #check to see if window size is greater than pattern, you need to shrink the window
    if len(str[left:right+1]) >= len(pattern): 
      char = str[left]
      left += 1
      if char in freq:
        if freq[char] == 0:
          matched -= 1
        freq[char] += 1

  
  return result_indices