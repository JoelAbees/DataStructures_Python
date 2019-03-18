class Queue:
    def __init__(self):
        self.q = []
    def isEmpty(self):
        print(len(self.q)<1)
    def enqueue(self, data):
        self.q.insert(0,data)
    def dequeue(self):
        print(self.q.pop())
    def size(self):
        print(len(self.q))
    def peak(self):
        print(self.q[len(self.q)-1])
    
    
q = Queue()
q.isEmpty()    
q.enqueue(6)
q.peak()
q.isEmpty()
q.enqueue(5)
q.enqueue(4)
q.enqueue(3)
q.enqueue(2)
q.enqueue(1)
q.peak()
q.dequeue()
q.peak()
