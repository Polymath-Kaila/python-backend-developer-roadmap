# 2. When a List Is Not the Answer

Lists are general containers but not optimized for:
- fast left pops → use deque
- numeric data → use array
- binary slicing → use memoryview
- thread-safe queues → use queue.Queue
- async queues → use asyncio.Queue
- sliding windows → use deque(maxlen)
- priority scheduling → use heapq
- sorted insertions → use bisect
- mutable binary data → use bytearray

Choose the right tool based on behavior and performance, not convenience.
