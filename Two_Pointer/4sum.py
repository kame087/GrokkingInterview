def search_quadruplets(arr, target):

  """
    HIGH LEVEL:
      You want to use the two pointer technique.
      Basically want you're doing is the Two Sum compartmentalized to benefit 4Sum.
      First you want to sort the array.
      Second you want to iterate the list i 0->n-4:
        * check for duplicate values
        iterate the list j = i+1 -> n-3:
          * check for duplicate values
          ** perform two sum pointer technique
          ** you can modularize this so that it's cleaner.
          * basically for each arr[i] and subsequent arr[j] you want to use the two pointer technique for the ranges from j+1 -> len(arr) - 1
          EVERYTHING BELOW THIS CAN BE ITS OWN FUNCTION:
          left = j + 1, right = len(arr) - 1
          while left < right:
            * calculate the total = arr[i] + arr[j] + arr[left] + arr[right] # left = j + 1, right = len(arr) - 1 aka the ranges
            if total == target_sum:
              append [arr[i], arr[j], arr[left], arr[right]] to the quadruplets list
              * check for duplicates:
              while left < right and arr[left] == arr[left-1]:
                left += 1
              while left < right and arr[right] == arr[right+1]:
                right -= 1
            else if total < target_sum:
              increment left pointer
            else:
              decrement right pointer # because total > target_sum

    Time: O(n^3), because the search_pairs executes O(n) for every iteration of the nexted loops which is O(n^2)
    Space: O(n), ignoring the output array, O(n) is required for sorting.
  
  """
  quadruplets = []
  
  arr.sort()
  for i in range(0, len(arr) - 3):
    if i > 0 and arr[i] == arr[i - 1]: # skip duplicates
      continue
    for j in range(i + 1, len(arr) - 2):
      if j > i + 1 and arr[j] == arr[j - 1]: # skip duplicates
        continue
      search_pairs(arr, target, i, j, quadruplets)
  return quadruplets

def search_pairs(arr, target_sum, first, second, quadruplets):
  # this function is basically the two pointer technique
  left = second + 1
  right = len(arr) - 1
  while (left < right):
    total = arr[first] + arr[second] + arr[left] + arr[right]
    if total == target_sum:
      quadruplets.append([arr[first], arr[second], arr[left], arr[right]])
      left += 1
      right -= 1
      while (left < right and arr[left] == arr[left - 1]): # skip duplicates
        left += 1
      while (left < right and arr[right] == arr[right + 1]): # skip duplicates
        right -= 1
    elif total < target_sum:
      left += 1
    else:
      right -= 1


def main():
  print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
  print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))

main()
