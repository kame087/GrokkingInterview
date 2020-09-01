def search_triplets(arr):
  """
    HIGH LEVEL:
      You want to have a similar approach to the two sum problem.
      * First you want to sort the array so that you can take advantage of the two pointer approach.
      * Iterate i: 0 -> n - 3:
        * left pointer = i + 1
        * right pointer = n - 1
        * while left < right:
          calculcate sum
          check if sum == 0:
            add triplet array to output array
            increment left
            decrement right
          else if sum < 0:
            increment left
          else:
            decrement right

      Time: O(n log n)
      Space: O(n)
  
  """
  triplets = []
  n = len(arr)
  arr.sort()
  
  for pointer in range(0,n-2):
    left = pointer + 1
    right = n - 1
    while left < right:
      total = arr[pointer] + arr[left] + arr[right]
      if total == 0:
        triplet = [arr[pointer], arr[left], arr[right]]
        triplets.append(triplet)
        left += 1
        right -= 1
      elif total < 0:
        left += 1
      else:
        right -= 1
  return triplets

def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))

main()

