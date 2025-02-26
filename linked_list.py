class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"<Node|{self.value}>"



class SinglyLinkedList:
    def __init__(self):
        # set the .head attribute to point to None to start (an empty Linked List)
        self.head = None

    # Method to add a new node to the beginning of the Linked List
    def push(self, new_value): # O(1) - Constant Time
        # Create a new node with the value passed in to the method
        new_node = Node(new_value)
        # Set the new node's .next attribute to be the front of the linked list (aka the head)
        new_node.next = self.head
        # Set the new node to be the beginning of the list (aka the head)
        self.head = new_node

    # Method to add a new node to the end of the Linked List
    def append(self, new_value): # O(n) - Linear Time
        # Create a new node with the value pass in to the method
        new_node = Node(new_value)
        # If the linked list is empty
        if self.head is None:
            # Set the new node as the first element in the list
            self.head = new_node
        # If not empty
        else:
            # Start at the first node
            current_node = self.head
            # Keep moving until the current_node has no next 
            while current_node.next is not None:
                # Move on to the next node
                current_node = current_node.next
            # Once current_node.next is None, set it to be the new node
            current_node.next = new_node

    # Method to print out all of the nodes in the linked list in order
    def traverse(self): # O(n) - Linear Time 
        print('Linked List Elements:')
        # Start at the beginning of the list
        print('head\n | \n V')
        current = self.head
        # While current is a node and not None
        while current:
            # Print the node with an arrow
            print(current, end=' -> ')
            # Move on to the next node in the linked list
            current = current.next
        # Print None at the end
        print(None)

    # Method to get a node by value
    def get_node(self, value_to_get): # O(n) - Linear
        # Start with the beginning
        node_to_check = self.head
        # While node_to_check is a node
        while node_to_check:
            # Check if this is the node we are looking for
            if node_to_check.value == value_to_get:
                # we foun the node, return it
                return node_to_check
            # if not, move to the next node
            node_to_check = node_to_check.next
        # If the node_to_check becomes None, we know the value is not in the linked list
        return None

    # Method to insert a new node into the linked list after a certain node (by value)
    def insert_after(self, prev_value, new_value): # O(n) - Linear
        # Get the previos node by value
        prev_node = self.get_node(prev_value)
        # Make sure that the prev_node exists
        if prev_node is None:
            print(f"{prev_value} is not in the linked list")
        else:
            # Create a new node with the new value
            new_node = Node(new_value)
            # point the new_node's .next to the prev_node's .next
            new_node.next = prev_node.next
            # point the prev_node's .next at the new node
            prev_node.next = new_node

    # Method to remove a node from the Linked List
    def remove(self, value_to_remove):
        # Check if the list is empty
        if self.head is None:
            print('List is empty, nothing to remove')
            return
        # If the first node is the node we are trying to removing
        if self.head.value == value_to_remove:
            # Set the .head attribute to be the next node
            self.head = self.head.next
            return
        # Start at the first node
        current_node = self.head
        # While the current node has a next node
        while current_node.next:
            # If the next node is the one we are trying to remove
            if current_node.next.value == value_to_remove:
                # Set the current node's next to be its next's next node
                current_node.next = current_node.next.next
                return
            # If not, move on to the next node
            current_node = current_node.next
        # If we get to the end of the Linked List without returning, the node was never there
        print(f"{value_to_remove} is not in this Linked List.")



months = SinglyLinkedList()
months.append('July')
months.append('August')
months.append('September')
months.push('May')
months.push('April')
months.append('Codember')
months.push('March')
months.append('October')
months.push('February')
months.insert_after('May', 'June')
months.push('January')
months.append('December')
months.insert_after('October', 'November')
months.remove('Codember')

months.traverse()


# ==============================================================================================================================

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"<Node|{self.value}>"


class DoublyLinkedList:
    def __init__(self):
        # set the .head attribute to point to None to start (an empty Linked List)
        self.head = None

    # Method to add a new node to the beginning of the Linked List
    def push(self, new_value): # O(1) - Constant Time
        # Create a new node with the value passed in to the method
        new_node = Node(new_value)
        # If there is a node at the head
        if self.head:
            # Set the head's previous node to be the new node
            self.head.prev = new_node
        # Set the new node's .next attribute to be the front of the linked list (aka the head)
        new_node.next = self.head
        # Set the new node to be the beginning of the list (aka the head)
        self.head = new_node

    # Method to add a new node to the end of the Linked List
    def append(self, new_value): # O(n) - Linear Time
        # Create a new node with the value pass in to the method
        new_node = Node(new_value)
        # If the linked list is empty
        if self.head is None:
            # Set the new node as the first element in the list
            self.head = new_node
        # If not empty
        else:
            # Start at the first node
            current_node = self.head
            # Keep moving until the current_node has no next 
            while current_node.next is not None:
                # Move on to the next node
                current_node = current_node.next
            # Once current_node.next is None, set it to be the new node
            current_node.next = new_node
            # Set the new_node's previous to be the current node
            new_node.prev = current_node

    # Method to print out all of the nodes in the linked list in order
    def traverse(self): # O(n) - Linear Time 
        print('Linked List Elements:')
        # Start at the beginning of the list
        print('head\n | \n V')
        current = self.head
        # While current is a node and not None
        while current:
            # Print the node with an arrow
            print(current, end=' <--> ')
            # Move on to the next node in the linked list
            current = current.next
        # Print None at the end
        print(None)

    # Method to get a node by value
    def get_node(self, value_to_get): # O(n) - Linear
        # Start with the beginning
        node_to_check = self.head
        # While node_to_check is a node
        while node_to_check:
            # Check if this is the node we are looking for
            if node_to_check.value == value_to_get:
                # we foun the node, return it
                return node_to_check
            # if not, move to the next node
            node_to_check = node_to_check.next
        # If the node_to_check becomes None, we know the value is not in the linked list
        return None

    # Method to insert a new node into the linked list after a certain node (by value)
    def insert_after(self, prev_value, new_value): # O(n) - Linear
        # Get the previos node by value
        prev_node = self.get_node(prev_value)
        # Make sure that the prev_node exists
        if prev_node is None:
            print(f"{prev_value} is not in the linked list")
        else:
            # Create a new node with the new value
            new_node = Node(new_value)
            # point the new_node's .next to the prev_node's .next
            new_node.next = prev_node.next
            # if the previous node has a next
            if prev_node.next:
                # Set the previous node's next .prev to be the new node
                prev_node.next.prev = new_node
            # point the prev_node's .next at the new node
            prev_node.next = new_node
            # new node's .prev to the previous node
            new_node.prev = prev_node

    # Method to remove a node from the Linked List
    def remove(self, value_to_remove):
        # Check if the list is empty
        if self.head is None:
            print('List is empty, nothing to remove')
            return
        # If the first node is the node we are trying to removing
        if self.head.value == value_to_remove:
            # Set the .head attribute to be the next node
            self.head = self.head.next
            # If the new head is a node
            if self.head:
                self.head.prev = None
            return
        # Start at the first node
        current_node = self.head
        # While the current node is not None
        while current_node:
            # If the current node is the one we are trying to remove
            if current_node.value == value_to_remove:
                # Adjust the pointers
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                return
            # If not, move on to the next node
            current_node = current_node.next
        # If we get to the end of the Linked List without returning, the node was never there
        print(f"{value_to_remove} is not in this Linked List.")


days = DoublyLinkedList()
days.push('Monday')
days.append('Thursday')
days.append('Saturday')
days.push('Sunday')
days.insert_after('Monday', 'Tuesday')
days.insert_after('Tuesday', 'Wednesday')
days.insert_after('Thursday', 'Friday')

days.remove('Sunday')
days.remove('Wednesday')

days.traverse()

