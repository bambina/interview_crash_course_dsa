# Example 2:
# Given the head of a linked list, determine if the linked list has a cycle.


class Node:
  def __init__(self, data):
    self.val = data
    self.next = None


def has_cycle(head: Node) -> bool:
  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
      return True
  return False


def to_linked_list(arr: list[int], cycle: bool = False) -> Node:
  head = Node(arr[0])
  curr = head
  for v in arr[1:]:
    node = Node(v)
    curr.next = curr = node

  if cycle:
    curr.next = head

  return head


test_cases = [
    (to_linked_list([1, 2, 3, 4, 5]), False),
    (to_linked_list([1, 2, 3, 4, 5], True), True),
]

for head, expected in test_cases:
  result = has_cycle(head)
  assert result == expected, f"Error: expected {expected}, got {result}"
