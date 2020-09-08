def smallest_subarray_with_given_sum(s, arr):
  
  """
  HIGH LEVEL:
    Use the sliding window technique to optimize time complexity.
    expand window until the running sum is greater that s.
    
    traverse array and expand window using right iterator
      add number @right to running sum
      while running sum is greater than s:
        update min_length = min(min_length, length of current window)
        subtract the value at the left side of the window
        shrink window by updating left side. i.e. (left += 1) 

  """
  curr_sum, left, min_length = 0, 0, float("inf")

  for right in range(len(arr)):
    curr_sum += arr[right]
    while curr_sum >= s:
      min_length = min(min_length, len(arr[left:right+1]))
      curr_sum -= arr[left]
      left += 1

  
  if min_length != float("inf"):
    return min_length
  
  return -1
