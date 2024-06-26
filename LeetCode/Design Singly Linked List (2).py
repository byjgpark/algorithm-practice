# Singly Linked List Node
class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node
    
    # def __str__(self):
    #     return f"self.data : {self.val} || self.next : {self.next}"    
    def __str__(self):
        return f"self.data : {self.val} || self.next : {self.next}"    

# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with a 'dummy' node which makes 
        # removing a node from the beginning of list easier.
        # self.head = None
        # self.head = ListNode(-1)
        self.head = None
        self.tail = self.head
    
    def get(self, index: int) -> int:
        # print("check self.head", self.head)
        # print("check self.tail", self.tail)
        curr = self.head
        i = 0
        # print("check curr" + curr)
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1  # Index out of bounds or list is empty

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        
        # print("check new_node",new_node) 
        print("check new_node",new_node) 
        
        current = self.head
        
        # print("check current",current)
        print("check current",current)
        
        self.head = new_node
        
        # print("check new self.head",self.head)
        print("check new self.head",self.head)
        
        self.head.next = current
        
        # print("check self.head at the end of function", self.head)
        print("check self.head at the end of function", self.head)
        
        if not current:
            self.tail = new_node
        # print("Check self.tail at the end of function :", self.tail)
        # print("--------------------------------------------------------")
        
        # new_node = ListNode(val)
        # new_node.next = self.head.next
        # print("check new_node.next", new_node.next)
        # self.head.next = new_node
        # print("self.head.next", self.head.next)
        # print("check new_node", new_node)
        # print("check self.head", self.head)
        # if not new_node.next:  # If list was empty before insertion
        #     self.tail = new_node
        # print("Check self.tail at the end of function :", self.tail)
        # print("--------------------------------------------------------")
    
    def insertTail(self, val: int) -> None:
        # print("check self.head", self.head.next)
        # print("check self.tail =", self.tail)
        print("check self.tail =", self.tail)
        self.tail.next = ListNode(val)
        # print("check self.tail in the middle =", self.tail)
        
        print("check self.tail in the middle =", self.tail)
        # print("check self.tail.next in the middle =", self.tail.next)
        self.tail = self.tail.next
        # print("check self.tail at the end of insertTail =",self.tail)
        print("check self.tail at the end of insertTail =",self.tail)

    
    def remove(self, index: int) -> bool:
        
        i = 0
        # prev = self.head
        curr = self.head
        # print("check self.head :",self.head)
        print("check curr from remove function : ",curr)
        # print("check index :",index, "| i :",i)
        # print("check i :",i, "| index :",index)
        while i < index and curr:
            i += 1
            prev = curr
            curr = curr.next
            # print("Check curr i < index : ", curr)
            # print("check i :",i, "| index :",index)
            
        print("------------------------------------------------------------------------------------")
        
        # print("Before if-statement prev :", prev)
        print("Before curr if-statement prev :", curr)
        print("before curr.next if-statement Check curr of curr and curr :", curr.next)
        
        # Remove the node ahead of curr
        if curr:
            # print("Before Check prev of curr and curr :", prev)
            print("Before Check curr of curr and curr.next :", curr)
            print("Before Check curr.next of curr and curr.next :", curr.next)
            print("Before self.tail of curr and curr.next :", self.tail)
            # print("Before Check curr.next of curr and curr.next.next :", curr.next.next)
            # print("Check curr.next.next of curr and curr.next :", curr.next.next)
            # print("check curr :", curr)
            # print("check.next :", curr.next)
            if curr == self.tail:
                print("check this if-statement gets executed")
                # print("Check curr.next == self.tail :", curr)
                self.tail = prev
            # print("Check curr.next : in the while-loop : ", curr.next)
            # print("Check curr.next.next : in the while-loop : ", curr.next.next)
            print("------------------------------------------------------------------------------------")
            # print("Right Before Check prev of curr and curr :", prev)
            print("Right Before Check curr.next of curr and curr.next :", curr.next)
            prev.next = curr.next
            # print("Right After Check prev of curr and curr :", prev)
            print("After check curr.next :",curr)
            print("After check curr.next.next :",curr.next)
            # curr = curr.next
            # print("After Check curr of curr and curr :", curr)
            # print("After Check curr.next of curr and curr.next :", curr.next)
            # print("After Check curr.next.next of curr and curr.next :", curr.next.next)
            # print("Check curr.next : in the while-loop : ", curr.next)
            # print("Check curr at the end of function :", curr)
            # print("Check self.head : at the end of if-statement : ", self.head)
            print("Check self.tail : at the end of if-statement : ", self.tail)
            return True
        # print("checking false statement here")
        return False

    def getValues(self) -> list[int]:
    #     # print("check curr" + curr)
    #     # print("check self.head", self.head)
    #     # curr = self.head
    #     # res = []
    #     # while curr:
    #     #     # print("check curr", curr)
    #     #     res.append(curr.val)
    #     #     curr = curr.next
    #     # return res        
    #     #---------------------------------
    
        print("Check self.head from the getValues :", self.head)
        # print("Check self.head from the getValues :", self.head)
        
        curr = self.head
        # print("Check curr", )
        res = []
        while curr:
            # print("Check curr", curr)
            res.append(curr.val)
            curr = curr.next
        return res
       
if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.insertHead(3)
    linkedList.insertHead(1)
    linkedList.insertHead(0)
    linkedList.insertTail(9)
    # linkedList.insertHead(0)
    # linkedList.insertTail(9)
    # linkedList.insertTail(4)
    # linkedList.insertTail(2)
    linkedList.remove(0)
    # linkedList.remove(3)
    print("Get Values : ", linkedList.getValues())