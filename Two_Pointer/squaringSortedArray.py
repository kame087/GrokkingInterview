def make_squares(arr):

  """
    HIGH LEVEL:
      You want to use the two pointer approach to get to the optimized solution.
      Because you may have negative numbers, you want the two pointers to start at opposite ends.
      compare each square and add the bigger square to the end of the list using a "bookmark" index.

      squares = [0] * len(arr) # this is the array we will return
      index = len(arr) - 1 # this is the "bookmark"
      left, right = 0, len(arr) - 1 # the two pointers

      while left <= right:
        * calculate square of @left and @right
        * if @right >= @left:
          * add @right square to squares[index]
          * decrement right
        * else @left is greater:
          * add @left square to squares[index]
          * increment left
        * decrement index for next iteration.

      * return squares array

    Time: O(n), n = len(arr)
    Space: O(n), n = len(arr)
  
  """
  squares = [0] * len(arr)
  index = len(arr) - 1
  left = 0
  right = len(arr) - 1

  while left <= right:
    left_square = arr[left] * arr[left]
    right_square = arr[right] * arr[right]
    if right_square >= left_square:
      squares[index] = right_square
      right -= 1
    else:
      squares[index] = left_square
      left += 1
    index -= 1

  return squares

def main():
  print(make_squares([-2, -1, 0 ,2, 3]))
  print(make_squares([-3, -1, 0, 1, 2]))

main()