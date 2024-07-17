class BinaryHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, key):
        self.heap.append(key)
        print("check key", key, "len(self.heap)", len(self.heap)-1, "self.heap", self.heap)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        print("check Int", -1//2)
        print("check parent_index : ", parent_index)
        while parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index
            print("check index inside of while", index)
            parent_index = (index - 1) // 2
            print("2nd check parent_index", parent_index)

    def get_min(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def delete_min(self):
        if self.is_empty():
            return None
        
        # find min value 
        min_value = self.heap[0]
        
        # assign the last index at the first index
        self.heap[0] = self.heap[-1]
        print("Check self.heap", self.heap)
        # pop the duplicate value
        self.heap.pop()
        print("Check self.heap after popping up", self.heap)
        # heapify down the min value from the tree 
        self._heapify_down(0)

        return min_value

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)


# Example Usage
if __name__ == "__main__":
    
    heap = BinaryHeap()

    # Insert elements
    heap.insert(3)
    heap.insert(2)
    heap.insert(15)
    heap.insert(5)
    heap.insert(4)
    heap.insert(45)

    print("Minimum element in the heap:", heap.get_min())

    # Delete minimum element
    print("Deleted minimum element:", heap.delete_min())

    print("Minimum element in the heap after deletion:", heap.get_min())
    
    print("check array heap", heap.heap)
    
    arr = [1,2,3,4]
    
    arr.pop()

