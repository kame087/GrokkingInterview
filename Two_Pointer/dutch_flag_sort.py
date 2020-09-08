def dutch_flag_sort(arr):
  """
    HIGH LEVEL:
      For the optimized solution, you want to use the two pointer technique.
      You'll have two pointers left and right, left pointing to the first element, right pointing to the last.
      You'll have a traveling pointer that iterates the entire array.
      Left & right are the placeholder pointers, which we'll use to swap elements around based on what value the traveler pointer is.
      while traveler <= right:
        do processing based on what arr[traveler] is
        if arr[traveler] == 0:
          swap arr[traveler] and arr[left]
          increment both traveler and left pointers
        else if arr[traveler] == 1:
          * carry on and don't swap anything.
          increment traveler
        else: # (arr[traveler] == 2)
          swap arr[traveler] and arr[right]
          decrement right, because after swapping, element @traveler may need to swapped again.

      return the original array now sorted.

    Time: O(n)
    Space: O(1)
  """
  traveler, left, right = 0, 0, len(arr) - 1
  while traveler <= right:
    if arr[traveler] == 0:
      arr[traveler], arr[left] = arr[left], arr[traveler]
      left += 1
      traveler += 1
    elif arr[traveler] == 2:
      arr[traveler], arr[right] = arr[right], arr[traveler]
      right -= 1
    else:
      traveler += 1
  return arr

def main():
  print(dutch_flag_sort([1, 0, 2, 1, 0]))
  print(dutch_flag_sort([2, 2, 0, 1, 2, 0]))

main()
