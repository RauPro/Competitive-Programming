import sys, bisect

input = lambda: sys.stdin.readline().rstrip("\r\n")
flush = lambda: sys.stdout.flush()
print = lambda *args, **kwargs: sys.stdout.write(' '.join(map(str, args)) + kwargs.get("end", "\n")) and flush()
def ints(): return map(int, input().split())
def strs(): return input().split()
def chars(): return list(input().strip())
def mat(n): return [list(ints()) for _ in range(n)]

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next= None

def main():
    n = int(input())
    get_node = [Node(i + 1) for i in range(n)]
    head = get_node[0]
    for i in range(n-1):
        c, a = strs()
        a = int(a)
        if c == 'a':
            get_node[i + 1].prev = get_node[a - 1]
            get_node[i + 1].next = get_node[a - 1].next
            get_node[a - 1].next = get_node[i + 1]
            if get_node[i + 1].next:
                get_node[i + 1].next.prev = get_node[i + 1]
        else:
            get_node[i + 1].next = get_node[a - 1]
            get_node[i + 1].prev = get_node[a - 1].prev
            get_node[a - 1].prev = get_node[i + 1]
            if get_node[i + 1].prev:
                get_node[i + 1].prev.next = get_node[i + 1]
            else:
                head = get_node[i + 1]
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    main()
