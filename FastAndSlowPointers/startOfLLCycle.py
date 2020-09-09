from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def find_cycle_start(head):
  """
    HIGH LEVEL:
      There's a famous algorithm that finds the start of the LL cycle, and I can't remember the name of it.
      But this is it.
      You use a fast and slow pointer technique, similar to finding a LL cycle.
      Once the fast and slow pointer meet.
      Set fast = head
      while fast and fast.next:
        check if fast  == slow:
          return fast
        move both slow and fast one node at a time.

    Time: O(n)
    Space: O(1)

  """
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      fast = head
      while fast and fast.next:
        if slow == fast:
          return fast
        fast = fast.next
        slow = slow.next
        
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
