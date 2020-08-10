def non_repeat_substring(str):
  """
    HIGH LEVEL:
      You want to use a  sliding window technique to expand and shrink whenever you meet the constraint.
      I used a set to keep track of the unique characters
      You traverse through the string:
        if the char is in the set, youre essentially starting the window from there:
          - First update the max length so far
          - max_length = max(max_length, len(str[left:right]))
          - clear the set
          - add char to set
          - left becomes right
        else:
          add char to set
        update right i.e. right += 1

      Time Complexity: O(n), since we're traversing the entire string
      Space: O(k), k = unique chars, but if we're strictly talking alphabet, it's O(26) -> O(1) this can be argued.

  
  """
  left = 0
  max_length = 0
  chars = {}

  for right in range(len(str)):
    char = str[right]
    if char in chars:
      left = max(left, chars[char]+1)
    
    chars[char] = right
    
    max_length = max(max_length, len(str[left:right+1]))

  return max_length
  
