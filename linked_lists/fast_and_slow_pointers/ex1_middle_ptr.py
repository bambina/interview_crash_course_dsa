# Example 1: Given the head of a linked list with an odd number of nodes head,
# return the value of the node in the middle.
# For example, given a linked list that represents 1 -> 2 -> 3 -> 4 -> 5, return 3.


class Node:
  def __init__(self, data):
    self.val = data
    self.next = None


def get_middle(head: Node) -> int:
  fast = slow = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  return slow.val


def to_linked_list(arr: list[int]) -> Node:
  head = Node(arr[0])
  curr = head
  for v in arr[1:]:
    node = Node(v)
    curr.next = curr = node

  return head


test_cases = [
    (to_linked_list([1, 2, 3, 4, 5]), 3),
    (to_linked_list([7]), 7),
]

for head, expected in test_cases:
  result = get_middle(head)
  assert result == expected, f"Error: expected {expected}, got {result}"
