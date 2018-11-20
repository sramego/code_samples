# Insert into a sorted linked list

class Node():
    def __init__(self,data):
	self.data = data
	self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def sorted_insert(self,new_node):
        if self.head is None:
	    new_node.next = None
	    self.head = new_node
            return

        if self.head.data >= new_node.data:
	    new_node.next = self.head
	    self.head = new_node

        else:
	    current = self.head
	    while (current.next is not None and current.next.data < new_node.data):
		current = current.next
		
	    new_node.next = current.next
            current.next = new_node
        return

    def printList(self):
        temp = self.head
	while (temp):
	    print temp.data
	    temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    new_node = Node(5)
    llist.sorted_insert(new_node)
    new_node = Node(20)
    llist.sorted_insert(new_node)
    new_node = Node(10)
    llist.sorted_insert(new_node)
    new_node = Node(14)
    llist.sorted_insert(new_node)
    new_node = Node(19)
    llist.sorted_insert(new_node)
    print "Sorted Linked List "
    llist.printList()
