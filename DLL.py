class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        self.pre  = None


class DLL:
    def __init__(self,value):
        node = Node(value)
        self.head   = node
        self.tail   = node
        self.length = 1

    def append(self, data):
        node =  Node(data)
        if self.head is None:
            self.head = self.tail =  node
        else:
            self.tail.next = node
            node.pre  =  self.tail
            self.tail =  node
        self.length +=1
        return True
        


    def  printDLL(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp= temp.next
            
    def reverse(self):
        temp = self.head
        before = None
        while temp is not None:
            temp.pre  = temp.next
            temp.next = before
            before    =  temp
            temp      =  temp.pre
        self.head= before

dll = DLL(4)
dll.append(3)
dll.append(1)
dll.append(2)
dll.reverse()

dll.printDLL()