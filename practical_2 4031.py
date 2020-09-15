class Node: 

    def _init_ (self, element, next = None ):
        self.element = element
        self.next = next
    def display(self):
        print(self.element)

class LinkedList:
        
    def _init_(self):
        self.head = None
        self.size = 0
        
 
        
    def _len_(self):
        return self.size
    
    
    def is_empty(self):
        return self.size == 0 
    
    def display(self):
        if self.size == 0:
            print("No element")
            return 
        first = self.head
        print(first.element)
        first = first.next
        while first:
            
            print(first.element)
            first = first.next
    
    
    def add_head(self,e):
        temp = self.head 
        self.head = Node(e) 
        self.head.next = temp
        self.size += 1 
        
    def get_tail(self):
        last_object = self.head
        while (last_object.next != None):
            last_object = last_object.next
        return last_object
        
    
    def remove_head(self):
        if self.is_empty():
            print("Empty Singly linked list")
        else:
            print("Removing")
            self.head = self.head.next
            self.size -= 1
            
    def add_tail(self,e):
        new_value = Node(e)
        self.get_tail().next = new_value
        self.size += 1
        
    def find_second_last_element(self):
        #second_last_element = None
        
        
        if self.size >= 2:
            first = self.head 
            temp_counter = self.size -2
            while temp_counter > 0:
                first = first.next 
                temp_counter -= 1 
            return first
        
        
        else:
            print("Size not sufficient")
            
        return None

        
        
    def remove_tail(self):
        if self.is_empty():
            print("Empty Singly linked list")
        elif self.size == 1:
            self.head == None
            self.size -= 1
        else: 
            Node = self.find_second_last_element()
            if Node:
                Node.next = None
                self.size -= 1
                
    def get_node_at(self,index):
        element_node = self.head
        counter = 0
        if index > self.size-1:
            print("Index out of bound")
            return None
        while(counter < index):
            element_node = element_node.next
            counter += 1
        return element_node
  
        
                
    def remove_between_list(self,position):
        if position > self.size-1:
            print("Index out of bound")
        elif position == self.size-1:
            self.remove_tail()
        elif position == 0:
            self.remove_head()
        else:
            prev_node = self.get_node_at(position-1)
            next_node = self.get_node_at(position+1)
            prev_node.next = next_node
            self.size -= 1
            
    def add_between_list(self,position,element):
        if position > self.size:
            print("Index out of bound")
        elif position == self.size:
            self.add_tail(element)
        elif position == 0:
            self.add_head(element)
        else:
            prev_node = self.get_node_at(position-1)
            current_node = self.get_node_at(position)
            prev_node.next = element
            element.next = current_node
            self.size -= 1
        
    def search (self,search_value):
        index = 0 
        while (index < self.size):
            value = self.get_node_at(index)
            print("Searching at " + str(index) + " and value is " + str(value.element))
            if value.element == search_value:
                print("Found value at " + str(index) + " location")
                return True
            index += 1
        print("Not Found")
        return False
    
    def merge(self,linkedlist_value):
        if self.size > 0:
            last_node = self.get_node_at(self.size-1)
            last_node.next = linkedlist_value.head
            self.size = self.size + linkedlist_value.size
            
        else:
            self.head = linkedlist_value.head
            self.size = linkedlist_value.size
            
    
            
        
            
            
        
            
            

            
            

 
# 1,2, (size , 2 , SLE = 0)
# 1,2,3,5 (size , 3 , SLE = 1)

            
'''
l1 = 1,2,3,5
l2 = 3,5,6,7

l1.copy(l2)

l1 = 3,5,6,7

l1.head = l2.head
l1.size = l2.size

l1 = None
l2 = 1,2,3


l1.merge(l2) ? => l1 = 3,1,2,14,5,4,2,9,1,2,14,5,4,2,9,1,2,14,5,4,2,9,1,2,14,5,4,2,9
'''
