def triplet_with_smaller_sum(arr, target):
  """
    HIGH LEVEL:
      The optimized solution can be achieve using the two pointer approach.
      You first want to sort the array 
      iterate through array p = 0->n-3:
        calculate difference between target - arr[p]
        left = p + 1
        right = n -1
        while left < right:
          if arr[left] + arr[right] < difference:
            add the distance of right - left to count [since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between left and right to get a sum less than the target sum]
            increment left
          otherwise:
            decrement right

      return count

      Time: O(n^2), as we iterate through the array, searching for the values that fall under the constraint take O(n)
      Space: O(n), because of sorting
  """
  
  count = 0
  arr.sort()
  
  for pointer in range(len(arr) - 2):
    diff = target - arr[pointer]
    left = pointer + 1
    right = len(arr) - 1
    while left < right:
      total = arr[left] + arr[right]
      if total < diff:
        count += right - left
        left += 1
      else:
        right -= 1
        
  return count


def main():
  print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))

main()
