def longest_substring_with_k_distinct(str, k):
  """
    HIGH LEVEL:
      Whenever a problem asks for a max or min length with a certain constraint, it almost always calls for
      a sliding window approach.

      You want to maintain a hashmap to keep track of the contraint of k distinct character.
      Expand the window and update the hashmap with the number of times a char appears (i.e. keep track of freq)
      You want to update max_length whenever the length of the hashmap is greater than k.
      decrease the  frequency of the left pointer char
      if frequency hits 0, delete it from hashmap.
      update left pointer 

      Time: O(n)
      Space: O(k)


  """
  max_length = float("-inf")
  left = 0
  freq = {}

  for right in range(len(str)):
    if str[right] not in freq:
      freq[str[right]] = 0
    freq[str[right]] += 1

    # keep shrinking the window until we're left k distinct chars
    while len(freq) > k:
      freq[str[left]] -= 1
      if freq[str[left]] == 0:
        del freq[str[left]]
      left += 1
    
    # remember the max length so far
    max_length = max(max_length, len(str[left:right+1]))

  if max_length != float("-inf"):
    return max_length

  return -1
