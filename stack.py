class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        print(self.stack.pop())
    def peek(self):
        print( self.stack[len(self.stack) - 1])
    def size(self):
        print( len(self.stack))

s = Stack()
s.push(8)
s.push(0)
s.push(8)
s.push(9)
s.push(2)
s.push(2)
s.push(8)
s.push(3)
s.push(0)
s.push(3)
s.peek()
s.size()
s.pop()
s.pop()
s.peek()