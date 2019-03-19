class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        
        print(self.data , end = " ")
        
        if self.right:
            self.right.printTree()
        
        
    def insert(self,data):
        if self.data:
            
            if data < self.data:
                if self.left is None: self.left = Node(data)
                else: self.left.insert(data)
                
            elif data > self.data:
                if self.right is None: self.right = Node(data)
                else: self.right.insert(data)
            
        else:self.data = data
        
    def findValue(self,data):
        print("current Node = " + str(self.data))
        if data < self.data:
            if self.left is None : print( "Value not found" )
            else : self.left.findValue(data)
        
        if data > self.data:
            if self.right is None : print( "Value not found" )
            else: self.right.findValue(data)
        
        if data == self.data:
            print ("Value Found")
        
    
root = Node(8)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(11)
root.insert(5)
root.printTree()
print(root.findValue(2))