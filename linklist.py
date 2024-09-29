class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        


class Linkdlist:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail= new_node
        self.length = 1


    def printLL(self):
        temp = self.head
        count = 0
        while temp is not None:
            print("index" ,count, temp.value)
            count +=1
            temp = temp.next

        
    def append(self,value):
        new_node = Node(value)
        if self.head is None :
            self.head= new_node
            self.tail= new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        # for only one node
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    # In Remove we return nodes 
    def remove(self,index):
        if index < 0 and index > self.length:
            return None
        if index == 0 :
            return self.popFirst()
        if index == self.length -1:
            return self.pop()
        temp = self.head
        for _ in range(0,index):
            temp = temp.next
        temp2 = temp.next
        temp.next = temp2.next
        temp2.next = None
        self.length -=1
        return temp2
    
    def prepend(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length +=1
        newNode.next = self.head
        self.head = newNode
        self.length +=1
        return True
    

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return True

        temp = self.get(index)
        newNode = Node(value)
        if temp is not None: 
            newNode.next = temp.next
            temp.next = newNode
            return 
        else:
            return False
    def set_value( self, index, value):
        # if index > self.length or index < 0:
        #     return None
        # node=Node(value)
        # if self.length == 0:
        #     self.head = node
        #     self.tail = node
        #     self.length +=1
        # temp = self.head
        # for _ in range(0,index):
        #     temp = temp.next
        # node.next = temp.next
        # temp.value = node.value

        #  the above code will behave same as get
        temp = self.get(index)
        if temp is not None: 
            temp.value = value
            return True
        else: 
            return False
         
    
    def get (self, index):
        if index > self.length or index < 0:
            return None 
        temp = self.head
        for _ in range(0,index):
            temp = temp.next
        return temp
    
    def popFirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        self.length -=1
    # When we have one Item
        if self.length == 0:
            self.tail = None
        return temp
    
    # Very Important
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # take 2 more pointer
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after 

    def find_middle_ele(self):
        pass
link_List = Linkdlist(10)

link_List.append(15)
link_List.append(16)
link_List.append(17)
link_List.append(19)
link_List.append(180)
link_List.append(156)
link_List.set_value(5,800)
link_List.insert(0,1800)
link_List.reverse()
# link_List.prepend(160)
# link_List.popFirst()
# link_List.printLL()
# print(link_List.remove(2).value)
link_List.printLL()


# print(link_List.get(5))

# link_List.pop()
