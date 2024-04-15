# Singly Linked List Node
class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node
    
    def __str__(self):
        return f"self.data : {self.val} || self.next : {self.next}"    

# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with a 'dummy' node which makes 
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        # self.head = None
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
        # new_node = self.data : 1 || self.next : None 
        # print("check new_node :", new_node)
        # print("self.head :", self.head)
        # print("self.head.next :", self.head.next)
        new_node.next = self.head.next
        # print("check new_node.next", new_node.next)
        # print("check new_node :", new_node)
        self.head.next = new_node
        if not new_node.next:  # If list was empty before insertion
            # print("check if not new_node.next :", new_node)
            self.tail = new_node
        # print("check self.tail :", self.tail)

    def insertTail(self, val: int) -> None:
        # print("check self.tail", self.tail)
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        # print("check self.tail at the end of insertTail :",self.tail)

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head

        print("check curr from remove : ",curr)
        # print("check index :",index, "| i :",i)
        print("check i :",i, "| index :",index)
        while i < index and curr:
            i += 1
            curr = curr.next
            
        
        # Remove the node ahead of curr
        if curr and curr.next:
            # print("check curr :", curr)
            # print("check.next :", curr.next)
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True

        return False

    def getValues(self) -> List[int]:
        # print("check curr" + curr)
        # print("check self.head", self.head)

        curr = self.head.next
        res = []
        while curr:
            # print("check curr", curr)
            res.append(curr.val)
            curr = curr.next
        return res