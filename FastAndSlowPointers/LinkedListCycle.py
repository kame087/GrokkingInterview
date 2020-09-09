class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def has_cycle(head):
  """
    HIGH LEVEL:
      This particular problem is great for using a fast and slow pointer approach. If the linked list
      indeed has a cycle, then the fast pointer will eventually "lap" the slow pointer. If it never "laps"
      the slow pointer, then the linked list doesn't have a cycle.

      Here's how you do it:
      Have the slow and fast pointers, point to head
      while fast and fast.next are not NULL:
        move slow one spot
        move fast two spots
        check if slow == fast:
          return True

      return False # since the conditionally never triggered.

    Time: O(n)
    Space:  O(1)
  """
  slow = head
  fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
      
  return False


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  print("LinkedList has cycle: " + str(has_cycle(head)))

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))


main()
