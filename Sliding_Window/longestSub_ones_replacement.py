def length_of_longest_substring(arr, k):
  """
    HIGH LEVEL:
     Another sliding window problem. This is completely the same concept as Longest substring w/ same
     letters after replacement k.

     The advantage here is that we're only dealing with 1s and 0s. So we don't really need to keep track
     of a hashmap, we just need to keep track of how many 1s we have.

     max_ones = 0
     max_length = float("-inf")
     left = 0
     traverse the array:
      if the element at current index == 1:
        update max_ones 
      
      if the difference between current window and max_ones > k:
        first check if left side of window is == 1:
          decrease max_ones
        shrink window


      update max_length (max_length or len(arr[left:right+1]))

    return max_length

    Time: O(n), n = len(arr)
    Space: O(1)
    
  """
  max_ones = 0
  max_length = float("-inf")
  left = 0
  for right in range(len(arr)):
    if arr[right] == 1:
      max_ones += 1
    
    if len(arr[left:right+1]) - max_ones > k:
      if arr[left] == 1:
        max_ones -= 1
      left += 1
    
    max_length = max(max_length, len(arr[left:right+1]))

  return max_length



def main():
  print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
  print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))

main()