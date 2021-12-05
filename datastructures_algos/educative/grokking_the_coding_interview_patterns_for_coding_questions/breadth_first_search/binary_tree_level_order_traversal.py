import collections

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = []
  if root is None:
    return result
  q = collections.deque([root])
  while q:
    currlevel = []
    for _ in range(len(q)):
      node = q.popleft()
      currlevel.append(node.val)
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
    result.append(currlevel)
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()