def remove_duplicates(arr):
  """
    HIGH LEVEL:
      This is similar maneuvering to the dutch national flag problem.
      You want to use a two pointer approach: where you iterate the array and the left pointer acts as a bookmark of where the next unique number will land

      The first number in the array is never a duplicate, so you can ignore it.
      If the number you're currently on is unique; meaning that it's previous neighbor is less than the number:
        *place this new unique number at left index.
        *increment left and right pointer
      otherwise you've encountered another duplicate:
        * just move on to the next number in the array: increment right pointer

      return left pointer this will tell you the length of the new array with no duplicates.

      set the left and right pointer to 1
      while right < len(arr):
        if the number @right != number @right-1 (basically the number before it):
          arr[left] = arr[right]
          left += 1
          right += 1
        else:
          right += 1

      Time: O(n)
      Space: O(1)
  """
  left, right = 1, 1
  while right < len(arr):
    if arr[right] != arr[right-1]:
      arr[left] = arr[right]
      left += 1
    right += 1

  return left

  

  
def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))

main()