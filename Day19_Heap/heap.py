import heapq

# Create empty heap
heap = []

# Insert elements
heapq.heappush(heap, 10)
heapq.heappush(heap, 30)
heapq.heappush(heap, 20)
heapq.heappush(heap, 5)

print("Heap:", heap)

# Smallest element
print("Top Element:", heap[0])

# Remove smallest element
removed = heapq.heappop(heap)

print("Removed Element:", removed)

print("Heap after deletion:", heap)s