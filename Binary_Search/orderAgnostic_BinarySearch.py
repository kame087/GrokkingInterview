def binary_search(arr, key):
  """
    HIGH LEVEL:
      This is pretty simple, use a flag to determine if sorted order is ascending or descending.
      Then do usual binary search on the array. and use flag to determine what search space to search in.

      lo = 0
      hi = len(arr) - 1
      isAsc = arr[lo] < arr[hi]

      while lo <= hi:
        calculate mid
        if element @mid == key:
          return mid
        else if element @mid > key:
          if isAsc:
            hi = mid - 1
          else:
            lo = mid + 1
        else:
          if isAsc:
            lo = mid + 1
          else:
            hi = mid - 1
      
      if you can't find the key
      return - 1

      This will give us a Time complexity of O(log n) and Space of O(1)

  """
  lo = 0
  hi = len(arr) - 1
  isAsc = arr[lo] < arr[hi]

  while lo <= hi:
    mid = (lo + hi) // 2
    if arr[mid] == key:
      return mid
    elif arr[mid] < key:
      if isAsc:
        lo = mid + 1
      else:
        hi = mid - 1
    else:
      if isAsc:
        hi = mid - 1
      else:
        lo = mid + 1
  
  return -1

def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()