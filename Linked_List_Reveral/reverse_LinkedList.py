from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse(head):
  """
    HIGH LEVEL:
      You want to assign a traveling node ("node") to head
      Initialize a prev node to None.
      As you traverse the linked list, 
        * assign a temp node to node.next (because you don't want to lose it.)
        * node.next then becomes prev (this is the reversing)
        * update prev to node (since this will be next destination to node.next)
        * update node to temp (traversing to the next node)
      return prev (since "node" is None at this point, and head is the original "tail")

      Time: O(n), since we're traveling the entire linked list.
      Space: O(1), since we're not using additional space besides the three nodes for placeholding.

  """
  
  if head:
    node = head
    prev = None
    while node:
      temp = node.next
      node.next = prev
      prev = node
      node = temp

  return prev
  


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse(head)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
