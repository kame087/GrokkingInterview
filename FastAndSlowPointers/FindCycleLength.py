class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def find_cycle_length(head):
  """
    HIGH LEVEL:
      This is a slight variation to the LinkedList Cycle problem. The only difference is that 
      they're asking for the length of the cycle.
      You want to use the Fast and Slow pointer technique to find where the fast and slow pointer meet.
      Then immediately after, you want to use a traveling pointer that starts at the slow pointer and keep track of the distance traveled until
      it meets the slow pointer again. The distance traveled until it circles back to slow, is the length of the cycle

      Time: O(n)
      Space: O(1)
  
  """
  slow, fast = head, head

  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
    if slow == fast:
      return calc_cycle_length(slow)

  return 0

def calc_cycle_length(slow):
  curr = slow
  length = 0
  while True:
    curr = curr.next
    length += 1
    if curr == slow:
      break
  return length

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()