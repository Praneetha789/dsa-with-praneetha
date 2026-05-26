import heapq

# Create empty heap
heap = []

# Insert elements
heapq.heappush(heap, 10)
heapq.heappush(heap, 30)
heapq.heappush(heap, 20)
heapq.heappush(heap, 5)

print("Heap:", heap)

# Top element
print("Smallest Element:", heap[0])

# Remove top element
removed = heapq.heappop(heap)

print("Removed Element:", removed)

# Heap after deletion
print("Heap after deletion:", heap)