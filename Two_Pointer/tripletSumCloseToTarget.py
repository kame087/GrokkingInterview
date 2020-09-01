def triplet_sum_close_to_target(arr, target_sum):
  """
    HIGH LEVEL:
      This is a similar approach to triplet sum, with a little twist.
      You want to use a two pointer approach to solve it efficiently.
      Here's how it goes:
      Variables:
        closest_sum
        global_difference
        left, right pointers

      * Sort the array
      * iterate the array i 0 -> n-2:
        * use two pointer approach like in two sum
        * left = i + 1
        * right = n - 1
        * while left doesn't cross right:
          * calculate triplet_sum
          * first check if triplet_sum == target_sum:
            * return triplet_sum
          * else:
            * calculate the curr_difference between triplet_sum and target_sum
            * if the abs(curr_difference) is less than the global_difference:
              * closest_sum = triplet_sum
              * update global_difference
            * determine which pointer to move by checking if triplet_sum < or > than target_sum
            * if triplet_sum < target_sum:
              * increment left
            * else:
              * decrement right

      return closest_sum

    Time: O(n log n), because of sorting
    Space: O(n), because of sorting.
  
  """
  
  closest_sum = float("inf")
  difference = float("inf")
  arr.sort()
  for pointer in range(len(arr)-2):
    left = pointer + 1
    right = len(arr) - 1
    while left < right:
      triplet_sum = arr[pointer] + arr[left] + arr[right]
      if triplet_sum == target_sum:
        return triplet_sum
      else:
        curr_diff = triplet_sum - target_sum
        if abs(curr_diff) < difference:
          closest_sum = triplet_sum
          difference = abs(curr_diff)
        if triplet_sum < target_sum:
          left += 1
        else:
          right -= 1

  return closest_sum
