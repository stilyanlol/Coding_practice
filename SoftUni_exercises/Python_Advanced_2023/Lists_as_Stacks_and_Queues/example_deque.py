from collections import deque

example_deque = deque()
example_stack = []

for i in range(1, 6):
    example_deque.append(i)
    example_stack.append(i)

print(deque)

while example_deque:
    print(example_deque.popleft())

print(example_stack)

while example_stack:
    print(example_stack.pop())
