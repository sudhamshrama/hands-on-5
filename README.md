# hands-on-5
Build-Min-Heap

A min heap is a binary tree data structure that satisfies the heap property: for any given node i, the value of i is less than or equal to the values of its children nodes. This ensures that the minimum value is always at the root of the tree.

## Operations on a Min Heap:
- Heapify Down: This operation is used to maintain the heap property when an element is removed or replaced. It starts at the root and compares it with its children, swapping with the smaller child if necessary, and recursively applies the same operation on the swapped child until the heap property is restored.

- Heapify Up: This operation is used to maintain the heap property when a new element is added to the heap. It starts at the last node (which is appended to the end of the array) and compares it with its parent, swapping with the parent if necessary, and recursively applies the same operation on the parent until the heap property is restored.

- Build Min Heap: This operation is used to create a min heap from an arbitrary array of elements. It iterates through the array starting from the last non-leaf node  and performs heapify down on each node, effectively converting the array into a min heap.

- Insert: This operation adds a new element to the min heap while maintaining the heap property. It appends the new element to the end of the array and then performs heapify up on the newly added element.

- Pop Root: This operation removes and returns the minimum element (the root) from the min heap. It swaps the root with the last element in the array, removes the last element, and then performs heapify down on the root to restore the heap property.
