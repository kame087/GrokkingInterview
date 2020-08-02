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


def reverse_sub_list(head, p, q):
  """
    HIGH LEVEL:
      You want to use the in-place reversal of a L.L. to reverse the sublist with a slight alteration.
      You need to remember the node prior to the sublist that needs to reversed. And the first node in the sublist
      that needs to be reversed. You need to remember them because if you don't, there's no way to "attach them" to the rest
      of the sublist.

      assign curr = head
      have a counter initialized to 0
      traverse all the way to the pth node with a trailing prev node.
      while curr and count < p - 1:
        prev = curr
        curr = curr.next
        count += 1
      
      That piece of code leaves curr at the pth node while remembering the node before the reversal.

      SAVE THESE NODES in seperate node variables.
      last_before_reversal = prev
      last_in_sub = curr

      * This is where you'll do the reversal of the sublist: 
      assign count = p
      while curr and count < q + 1:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

      * This is where you're going link the nodes that you saved to their respective nodes:
      if prev:
        last_before_reversal.next = prev (in example: 1.next = 4)

      last_in_sub.next = curr (in example: 2.next = 5)

      return head

      Time: O(n)
      Space: O(1)

  
  """

  if p == q:
    return head
  
  count = 0
  curr, prev = head, None

  while curr and count < p-1:
    prev = curr
    curr = curr.next
    count += 1
  
  count = p
  last_before_sub = prev
  last_node_sub = curr

  while curr and count < q + 1:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
    count += 1

  if prev:
    last_before_sub.next = prev

  last_node_sub.next = curr


  
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
