from queue import Priorityqueue

pq = Priorityqueue()
pq.enqueue("http://example1.com", 5)
pq.enqueue("http://example2.com", 2)
pq.enqueue("http://example3.com", 8)
pq.enqueue("http://example4.com", 1)

print(pq.dequeue())
print(pq.dequeue())
