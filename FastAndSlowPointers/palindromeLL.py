class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def is_palindromic_linked_list(head):
  """
    Time: O(n)
    Space: O(n)
  """
  freq = {}
  length = 0

  node = head
  while node:
    if node.value not in freq:
      freq[node.value] = 0
    freq[node.value] += 1
    node = node.next
    length += 1

  for key in freq:
    if length % 2 == 0:
      if freq[key] % 2 != 0:
        return False
    else:
      if freq[key] % 2 != 0:
        if freq[key] > 1:
          return False


  return True



def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()







