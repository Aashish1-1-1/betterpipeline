class Priorityqueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def enqueue(self, url, weight):
        self.heap.append((url, weight))
        self._heapify_up(len(self.heap) - 1)

    def dequeue(self):
        if self.is_empty():
            print("Underflow")
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        url, weight = self.heap.pop()
        self._heapify_down(0)
        return url, weight

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[parent][1] < self.heap[index][1]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index

        if (
            left_child < len(self.heap)
            and self.heap[left_child][1] > self.heap[largest][1]
        ):
            largest = left_child
        if (
            right_child < len(self.heap)
            and self.heap[right_child][1] > self.heap[largest][1]
        ):
            largest = right_child
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self._heapify_down(largest)
