class Node:
    def __init__(self,value,nextNode=None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
            return
        self.tail.nextNode = newNode
        self.tail = newNode
    
    def delete(self, value):
        if not self.head:
            return
        
        currentNode = self.head
        previousNode = None

        while currentNode:
            if currentNode.value == value:
                if previousNode:
                    previousNode.nextNode = currentNode.nextNode
                else:
                    self.head = currentNode.nextNode
            previousNode = currentNode
            currentNode = currentNode.nextNode

    def deleteTail(self):
        currentNode = self.head
        if not currentNode:
            return None
        elif currentNode == self.tail:
            self.head = None
            self.tail = None
            return currentNode.value
        while currentNode.nextNode != self.tail:
            currentNode = currentNode.nextNode
        value = self.tail.value
        currentNode.nextNode = None
        self.tail = currentNode
        return value
    
    def search(self, value):
        currentNode = self.head
        while currentNode:
            if currentNode.value == value:
                return True
            currentNode = currentNode.nextNode
        return False
    
    def display(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.nextNode
        print("None")

if __name__ == "__main__":
    pass
