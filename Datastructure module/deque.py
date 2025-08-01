from collections import deque
d = deque(["mk", "ab", "abhi", "maj", "abhi", "mk"])
print(d)
d.append("ajay")
print(d)
d.appendleft("appendleft")
print(d)
d.rotate(2)
print(d)
