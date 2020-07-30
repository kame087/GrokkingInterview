def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  # BRUTE FORCE SOLUTION:
  # Time: O(n * k), Space: O(1)
  # max_sum = 0
  # for left in range(len(arr) - k):
  #   curr_sum = 0
  #   right = left
  #   while len(arr[left:right+1]) <= k:
  #     curr_sum += arr[right]
  #     right += 1
  #   max_sum = max(max_sum, curr_sum)

  # if max_sum > 0:
  #   return max_sum

  # Optimized solution
  # Time: O(n)
  # Space: O(1)

  max_sum, curr_sum, left = 0, 0, 0

  for right in range(len(arr)):
    curr_sum += arr[right]
    if right >= k -1:
      max_sum = max(max_sum, curr_sum)
      curr_sum -= arr[left]
      left += 1

  return max_sum


    
  
