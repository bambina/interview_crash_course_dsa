# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

class Node:
  def __init__(self, data):
    self.val = data
    self.next = None


def get_middle_node(head: Node) -> int:
  slow = fast = head

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
    (to_linked_list([1, 2, 3, 4, 5, 6]), 4),
    (to_linked_list([7]), 7),
]

for head, expected in test_cases:
  result = get_middle_node(head)
  assert result == expected, f"Error: expected {expected}, got {result}"
