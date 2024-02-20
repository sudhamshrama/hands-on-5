class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def build_min_heap(self, arr):
        self.heap = arr[:]
        n = len(arr)
        for i in range(n // 2, -1, -1):
            self.heapify_down(i)

    def heapify_down(self, i):
        smallest = i
        left = self.left(i)
        right = self.right(i)
        n = len(self.heap)
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def pop_root(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return root


# Example usage
if __name__ == "__main__":
    # Create a min heap and build it
    heap = MinHeap()
    heap.build_min_heap([4, 10, 3, 5, 1])
    print("Min Heap:", heap.heap)

    # Insert an element
    heap.insert(2)
    print("After Inserting 2:", heap.heap)

    # Pop the root element
    root = heap.pop_root()
    print("Popped Root:", root)
    print("Heap after popping root:", heap.heap)
