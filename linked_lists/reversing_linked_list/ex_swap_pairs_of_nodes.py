# Example:
# Given the head of a linked list, swap every pair of nodes.
# For example, given a linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6,
# return a linked list 2 -> 1 -> 4 -> 3 -> 6 -> 5.


class Node:
  def __init__(self, data):
    self.val = data
    self.next = None


def to_list(head: Node) -> list[int]:
  result = []
  curr = head
  while curr:
    result.append(curr.val)
    curr = curr.next
  return result


def swap_pairs(head: Node) -> list[int]:
  if not head or not head.next:
    return to_list(head)
  ans = head.next
  prev = None

  # B->A->D->C
  while head and head.next:
    if prev:
      prev.next = head.next     # A->D
    next_node = head.next.next  # C
    head.next.next = head  # B->A
    head.next = next_node  # A->C in case # of nodes is odd
    prev = head       # prev = A
    head = next_node  # head = C

  return to_list(ans)


def to_linked_list(arr: list[int]) -> Node:
  head = Node(arr[0])
  curr = head
  for v in arr[1:]:
    node = Node(v)
    curr.next = curr = node

  return head


test_cases = [
    (to_linked_list([1, 2, 3, 4, 5, 6]), [2, 1, 4, 3, 6, 5]),
    (to_linked_list([1, 2, 3, 4, 5]), [2, 1, 4, 3, 5]),
    (to_linked_list([1]), [1]),
    (to_linked_list([1, 2]), [2, 1]),
]

for head, expected in test_cases:
  result = swap_pairs(head)
  assert result == expected, f"Error: expected {expected}, got {result}"
