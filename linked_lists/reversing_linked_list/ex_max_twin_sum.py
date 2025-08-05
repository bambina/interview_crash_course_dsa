# In a linked list of size n, where n is even,
# the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node,
# if 0 <= i <= (n / 2) - 1.
# The twin sum is defined as the sum of a node and its twin.
# Given the head of a linked list with even length,
# return the maximum twin sum of the linked list.


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


def twin_sum(head: Node) -> int:
  # Find the middle node
  slow = fast = prev = head
  n = 0
  while fast and fast.next:
    n += 1
    prev = slow
    slow = slow.next
    fast = fast.next.next
  first_half_last = prev

  # Reverse the second half of the list
  prev = None
  curr = slow
  # null<-A<-B<-C
  while curr:
    next_node = curr.next  # B
    curr.next = prev  # null<-A
    prev = curr
    curr = next_node
  first_half_last.next = prev

  # Move a fast pointer n times
  fast = slow = head
  for _ in range(n):
    fast = fast.next

  ans = 0
  while fast:
    ans = max(ans, slow.val+fast.val)
    slow = slow.next
    fast = fast.next

  return ans


def to_linked_list(arr: list[int]) -> Node:
  head = Node(arr[0])
  curr = head
  for v in arr[1:]:
    node = Node(v)
    curr.next = curr = node

  return head


test_cases = [
    (to_linked_list([5, 4, 2, 1]), 6),
    (to_linked_list([4, 2, 2, 3]), 7),
    (to_linked_list([1, 100000]), 100001),
]

for head, expected in test_cases:
  result = twin_sum(head)
  assert result == expected, f"Error: expected {expected}, got {result}"
