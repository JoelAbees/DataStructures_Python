
class Node:
    def __init__(self, data =  None , next_node = None):
        self.data = data
        self.next_node = next_node    
    def getData(self):
        return self.data    
    def getNext(self):
        return self.next_node    
    def setNext(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.headVal = None        
    def printList(self):
        currentNode = self.headVal
        while currentNode is not None:
            print(currentNode.getData() , end = " ")
            currentNode = currentNode.next_node
        print(" ")        
    def insertAtBegining(self, newdata):
        newNode = Node(newdata)
        newNode.next_node = self.headVal
        self.headVal = newNode        
    def insertAtEnd(self,newData):
        newNode = Node(newData)
        if self.headVal is None:
            self.headVal = newNode
            return
        
        currentNode = self.headVal
        while (currentNode.next_node):
            currentNode = currentNode.next_node
        
        currentNode.next_node = newNode        
    def insertInbetween(self , nodeNumber, newData):
        count = 1
        currentNode = self.headVal
        while count < nodeNumber:
            print(currentNode.getData())
            currentNode = currentNode.next_node
            
            count += 1
        newNode = Node(newData)
        newNode.next_node = currentNode.next_node
        currentNode.next_node = newNode    
    def removeNode(self, Nodedata):
        currentNode = self.headVal
        while currentNode.getData() != Nodedata and currentNode.next_node is not None:
            prev = currentNode
            currentNode = currentNode.next_node
        if currentNode.getData() == Nodedata:
            prev.next_node = currentNode.next_node
            currentNode = None
        
        
ll1 = LinkedList() #CREATE LINKED LIST
ll1.headVal = Node("Mon")
e2 = Node("Tues")
e3 = Node("Wed")
ll1.headVal.next_node = e2
e2.next_node = e3  
ll1.printList()
ll1.insertAtBegining("Sat") #INSERT AT BEGINING
ll1.printList()
ll1.insertAtEnd("Friday") #INSERT AT END
ll1.printList()
ll1.insertInbetween(4, "Thursday") #INSERT IN BETWEEN
ll1.printList()
ll1.insertInbetween(1, "Sunday")
ll1.printList()
ll1.removeNode("Thursday") #DELETE NODE
ll1.printList()