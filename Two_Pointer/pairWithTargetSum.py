def pair_with_targetsum(arr, target_sum):
  """
    HIGH LEVEL:
      Use a two pointer approach:
        have one pointer in the beginning of the array "left"
        have another pointer at the end of the array "right"
        while the left doesn't cross the right:
          calculate sum by adding element @left + element @right
          if sum == target:
            return [left index, right index]
          elif sum > target:
            right -= 1
            * this means we need a smaller sum, so decrement the right pointer
          else:
            left += 1
            * this means we have a lower sum, so we increment the left pointer

        return [-1, -1] * this means we didn't find a pair in the array that equals target.

      Time: O(n)
      Space: O(1)
  
  """
  left = 0
  right = len(arr) - 1

  while left < right:
    total = arr[left] + arr[right]
    if total == target_sum:
      return [left, right]
    elif total > target_sum:
      right -= 1
    else:
      left += 1
  return [-1, -1]


def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
