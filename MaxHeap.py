class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, element):
        self.heap.append(element)
        self.heapify_up(len(self.heap) - 1)
    # moves the element up the tree until the heap structure is restored
    def heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)
    # moves the element down the tree until the heap structure is restored. Use this method in the heap sort method
    def heapify_down(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.heapify_down(largest)
    # search thru left and right subtrees recursively
    def search(self, index, element):
        if index >= len(self.heap):
            return False
        if self.heap[index] == element:
            return True
        if self.heap[index] < element:
            return False
        return self.search(self.left_child(index), element) or self.search(self.right_child(index), element)
    # returns a sorted list of elements in ascending order
    def sort(self):
        sorted_array = []
        original_heap = self.heap[:]
        original_size = len(self.heap)
        
        for i in range(original_size):
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            sorted_array.append(self.heap.pop())
            self.heapify_down(0)
        
        self.heap = original_heap  # restore the original heap
        sorted_array.reverse()  # reverse because we want ascending order
        return sorted_array

max_heap = MaxHeap()
elements = [101, 3, 1, 6, 5, 2, 4, 50, 11, 16, 19, 20]
for element in elements:
    max_heap.insert(element)

print("Heap:", max_heap.heap)
print("Search 5:", max_heap.search(0, 5))
print("Search 10:", max_heap.search(0, 10))
print("Sorted heap:", max_heap.sort())