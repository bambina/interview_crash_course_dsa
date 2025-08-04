# Example 3: Given the head of a linked list and an integer k,
# return the kth node from the end.
# For example, given the linked list that represents 1 -> 2 -> 3 -> 4 -> 5 and k = 2, return the node with value 4, as it is the 2nd node from the end.


class Node:
  def __init__(self, data):
    self.val = data
    self.next = None


def find_node(head: Node, k: int) -> int:
  fast = slow = head
  for _ in range(k):
    fast = fast.next

  while fast:
    slow = slow.next
    fast = fast.next

  return slow.val


def to_linked_list(arr: list[int]) -> Node:
  head = Node(arr[0])
  curr = head
  for v in arr[1:]:
    node = Node(v)
    curr.next = curr = node

  return head


test_cases = [
    (to_linked_list([1, 2, 3, 4, 5]), 2, 4),
    (to_linked_list([10, 20, 30]), 1, 30),
    (to_linked_list([7]), 1, 7),
]

for head, k, expected in test_cases:
  result = find_node(head, k)
  assert result == expected, f"Error: expected {expected}, got {result}"
