import sys 
class MaxHeap: 

    #Constructor
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1) 
        self.Heap[0] = sys.maxsize 
        self.Front = 1

    # Function to return the position of parent node
    def parent(self, pos):  
        return pos // 2

    # return the position of left child
    def leftChild(self, pos):  
        return 2 * pos 

    # return the position of right child    
    def rightChild(self, pos):     
        return (2 * pos) + 1


    # node is a leaf node; returns true if the passed 
    def isLeaf(self, pos):  
        if pos >= (self.size//2) and pos <= self.size: 
            return True
        return False

    # Function to swap two nodes of the heap 
    def swap(self, fpos, spos):         
        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos], self.Heap[fpos]) 

    # Function to heapify the node at pos 
    # heapify() converts the iterable into a heap data 
    def maxHeapify(self, pos): 

        if not self.isLeaf(pos): 
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or self.Heap[pos] < self.Heap[self.rightChild(pos)]): 

                if (self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]): 
                    self.swap(pos, self.leftChild(pos)) 
                    self.maxHeapify(self.leftChild(pos)) 

                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.maxHeapify(self.rightChild(pos)) 

    # Add a new patient 
    def addPatient(self, element): 
        if self.size >= self.maxsize: 
            return
        self.size += 1
        self.Heap[self.size] = element 
        current = self.size 
        while (self.Heap[current] > self.Heap[self.parent(current)]): 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 

    # Removing the patient with the highest priority from the queue and showing the patient with the highest priority
    def extractMax(self):  
        popped = self.Heap[self.Front] 
        self.Heap[self.Front] = self.Heap[self.size] 
        self.Heap[self.size] = 0
        self.size -= 1
        self.maxHeapify(self.Front) 
        return popped 

    # Merges Max heaps a[] and b[] into merged[] 
    def mergeHeaps(merged, a, b, n, m):

        for i in range(n):
            merged[i] = a[i]

        for i in range(m):
            merged[n + i] = b[i]
 
    # Function to print the contents of the heap 
    def Print(self): 
        for i in range(1, (self.size // 2) + 1): 
            print(" Parent : " + str(self.Heap[i]) +
            " Left Chide : " + str(self.Heap[2 * i]) +
            " Right Childs : " + str(self.Heap[2 * i + 1])) 


maxHeap = MaxHeap(25) 
maxHeap.addPatient(1) 
maxHeap.addPatient(3) 
maxHeap.addPatient(10)  
maxHeap.addPatient(8) 
maxHeap.addPatient(6) 
#Print before the highest priority is deleted
maxHeap.Print() 
print("The patient with the highest priority " + str(maxHeap.extractMax())) 
#Print after the highest priority is deleted
maxHeap.Print() 
    