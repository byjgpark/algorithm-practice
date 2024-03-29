# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __str__(self):
        return f"self.data : {self.data} | self.next : {self.next}"

class LinkedList:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        return f"self.head : {self.head}"

    def append(self, data):
        print("check data", data)
        print("check self.head", self.head)
        new_node = Node(data)
        # print("check new_node :", new_node)
        if not self.head:
            # print("check not self.head", self.head)
            self.head = new_node
            return
        last_node = self.head
    
        print("check last_node.next", last_node.next)
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    # linked_list.prepend(0)
    linked_list.display()  # Output: 0 -> 1 -> 2 -> 3 -> None
    # linked_list.delete_node(2)
    # linked_list.display()  # Output: 0 -> 1 -> 3 -> None
