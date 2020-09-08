from collections import deque

def find_subarrays(arr, target):
  """
    HIGH LEVEL:
      This problem follows the sliding window pattern.
      Since the problem asks for a list of subarrays that are less than target, the sliding window
      will continue expanding at every iteration as long as the product is less than the target
      while the product is greater or equal to the target, and the left of the window is less than the len(arr):
        you want to shrink the window by:
        dividing product by arr[left]
        increment left by 1
      at every iteration of the main loop, you will create a temporary queue
      Iterate i from the range: right -> left # !! This is because the product of all numbers from left to right are less than the product, you can add every subarray within this range.
        at every iteration to will enqueue arr[i] to the queue
        add the current queue (converted to a list) to the result list
        ** this part of the iteration process is what builds the subarrays.

    Time: O(n^2)
    Space: O(n^2)
  """

  result = []
  product = 1
  left = 0
  for right in range(len(arr)):
    product *= arr[right]
    while (product >= target and left < len(arr)):
      product /= arr[left]
      left += 1
    temp_list = deque()
    for i in range(right, left - 1, -1):
      temp_list.appendleft(arr[i])
      result.append(list(temp_list))

  return result

def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))


main()