# Given the head of a sorted linked list,
# delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

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


def remove_duplicates(head: Node) -> list[int]:
  curr = head
  while curr and curr.next:
    if curr.val == curr.next.val:
      curr.next = curr.next.next
    else:
      curr = curr.next
  return to_list(head)


def to_linked_list(arr: list[int]) -> Node:
  head = Node(arr[0])
  curr = head
  for v in arr[1:]:
    node = Node(v)
    curr.next = curr = node

  return head


test_cases = [
    (to_linked_list([1, 1, 1]), [1]),
    (to_linked_list([1, 1, 2]), [1, 2]),
    (to_linked_list([1, 1, 2, 3, 3]), [1, 2, 3]),
]

for head, expected in test_cases:
  result = remove_duplicates(head)
  assert result == expected, f"Error: expected {expected}, got {result}"
