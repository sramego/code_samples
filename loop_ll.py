# Detect loop in a linked list

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def push(self,data):
	new_node = Node(data)
	new_node.next = self.head
	self.head = new_node

    def detectRemoveloop(self):
        if self.head is None or self.head.next is None:
            return
        slow = self.head
        fast = self.head
        
        slow = slow.next
        fast = fast.next.next
        while fast:
	    if fast.next is None:
	        break
	    if slow == fast:
                # Found loop
                break
	    slow = slow.next
            fast = fast.next.next

        # if loop is present
        if slow == fast:
            slow = self.head
            while (slow.next != fast.next):
		slow = slow.next
		fast = fast.next

	    fast.next = None
   
    def printList(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(50)
    llist.head.next = Node(90)
    llist.head.next.next = Node(100)
    llist.head.next.next.next = Node(200)
    llist.head.next.next.next.next = Node(250)
    #creating a loop
    llist.head.next.next.next.next.next = llist.head.next
    #Detect n remove loop
    llist.detectRemoveloop()
    llist.printList()
