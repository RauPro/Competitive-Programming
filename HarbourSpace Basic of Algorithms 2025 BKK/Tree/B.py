import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

class Node:
    def __init__(self, value=None):
        self.right = None
        self.left = None
        self.val = value

    def insert(self, value):
        if self.val is None:
            self.val = value
        elif value < self.val:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def search(self, value):
        if self.val is None or self.val == value:
            return self
        if value < self.val:
            return self.left.search(value) if self.left else None
        else:
            return self.right.search(value) if self.right else None

    def remove(self, value):
        if self.val is None:
            return self
        if value < self.val:
            if self.left:
                self.left = self.left.remove(value)
        elif value > self.val:
            if self.right:
                self.right = self.right.remove(value)
        else:
            if not self.left and not self.right:
                return None
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            min_larger_node = self.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left
            self.val = min_larger_node.val
            self.right = self.right.remove(min_larger_node.val)
        return self

    def lower_bound(self, value):
        if self.val is None:
            return None
        if self.val >= value:
            left_result = self.left.lower_bound(value) if self.left else None
            return left_result if left_result is not None else self
        else:
            return self.right.lower_bound(value) if self.right else None


def main():
    n, m = ints()
    a = list(ints())
    BST = Node(None)
    for value in a:
         BST.insert(value)
    for i in range(m):
        q, x = strs()
        x = int(x)
        if q == '-':
            BST = BST.remove(x)
        elif q == '?':
            if BST is None or BST.val is None:
                print(-1)
            else:
                result = BST.lower_bound(x)
                if result:
                    print(result.val)
                else:
                    print(-1)


if __name__ == "__main__":
    main()