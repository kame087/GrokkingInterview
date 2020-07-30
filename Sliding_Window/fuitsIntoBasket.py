def fruits_into_baskets(fruits):
  """
    HIGH LEVEL:
      Similar approach to longest substring with k distinct characters,
      Except that k is always 2.

      Time: O(n)
      Space: O(1)

  """
  freq = {}
  max_length = 0
  left = 0

  # expand window until freq length is > 2
  for right in range(len(fruits)):
    if fruits[right] not in freq:
      freq[fruits[right]] = 0
    freq[fruits[right]] += 1

    # keep shrinking the window until we have 2 distinct characters in freq
    while len(freq) > 2:
      freq[fruits[left]] -= 1
      if freq[fruits[left]] == 0:
        del freq[fruits[left]]
      left += 1

    # remember max length up to this point
    max_length = max(max_length, len(fruits[left:right+1]))
  return max_length
