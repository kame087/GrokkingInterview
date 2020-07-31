def find_missing_number(nums):

  """
    HIGH LEVEL:
      You basically want to use a cyclic sort approach.
      The goal is to make sure that each element at index i is equal to the index.

      You iterate each number in the array
      if the number @i is less than the length of array and doesn't equal i:
        you need to swap them.
        array[i] = array[array[i]]
        array[array[i]] = array[i] # this is now in it's proper place
      otherwise i = number @i:
        increase i

      iterate the array again:
        if i != number @i:
          return i

      otherwise they're all in their proper place so return n
  
  """
  i, n = 0, len(nums)

  while i < n:
    index = nums[i]
    if nums[i] < n and nums[i] != nums[index]:
      nums[i], nums[index] = nums[index], nums[i]
    else:
      i += 1

  for i in range(n):
    if nums[i] != i:
      return i

  return n


  
