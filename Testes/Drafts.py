class ListNode:
    """Define a simple element (Node) for the list."""

    def __init__(self, data):
        self.data = data  # Store the value here.
        self.next = None  # Link to the next Node. Start is always None.

# --- 1. CORE FUNCTION: Generate Linked List ---

def generateLinkedList(input_array):
    """Make a Linked List from an array (list) and return the first node (head)."""
    if not input_array: # Testing Falsy
        return None

    head_node = ListNode(input_array[0])  # Make the Head Node (the start).
    current = head_node  # 'current' will help us link nodes as a temporary cursor.

    for data in input_array[1:]:  # Loop for all other items, starting in position 1 until the end.
        current.next = new_node = ListNode(data) # A new node is created using the input data.
        current = new_node  # Move 'current' to the new node for the next link.

    return head_node

# --- 2. TRAVERSAL / PRINT ---

def printLinkedList(head):
    """Walk through the list and print all data."""
    current_node = head
    output = ""
    while current_node:
        output += str(current_node.data) + " -> " # String concatenation (data must be cast)
        current_node = current_node.next  # Go to the next node using the 'next' pointer.
    print(output + "NULL")

# --- 3. INSERT AT BEGINNING (Head) ---

def insertAtStart(head, data):
    """Insert a new node at the beginning of the list."""
    new_node = ListNode(data)
    new_node.next = head  # New node points to the old head.
    return new_node  # Return the new head.

# --- 4. INSERT AFTER A SPECIFIC VALUE ---

def insertAfterValue(head, target_data, new_data):
    """Insert a new node AFTER the node that has 'target_data'."""
    current = head

    while current and current.data != target_data:  # Find the target node.
        current = current.next

    if current is None:
        print(f"Error: Target value '{target_data}' not found.")
        return head

    new_node = ListNode(new_data)

    # Change the links to put the new node in the middle:
    new_node.next = current.next  # New node links to the node after 'current'.
    current.next = new_node  # 'current' links to the new node.

    return head

# --- 5. DELETE BY VALUE ---

def deleteByValue(head, target_data):
    """Remove the first node that matches the given value."""
    current = head
    previous = None

    if current and current.data == target_data:  # Case 1: Deleting the Head
        return current.next  # Return the next node as the new head.

    while current and current.data != target_data:  # Case 2: Find the node, keeping track of 'previous'.
        previous = current  # 'previous' follows 'current'.
        current = current.next

    if current is None:  # Value was not found.
        print(f"Error: Value '{target_data}' not found for deletion.")
        return head

    # Case 3: Deleting in the middle/end: 'previous' skips 'current'.
    previous.next = current.next
    return head

# --- EXAMPLE EXECUTION ---

print("--- LINKED LIST DEMO ---")
initial_data = [10, 20, 30]
my_list_head = generateLinkedList(initial_data)
print("\n1. Initial List:")
printLinkedList(my_list_head)

my_list_head = insertAtStart(my_list_head, 5)
print("\n2. Changing the head value:")
printLinkedList(my_list_head)

my_list_head = insertAfterValue(my_list_head, 20, 25)
print("\n3. After Inserting '25' after '20':")
printLinkedList(my_list_head)

my_list_head = deleteByValue(my_list_head, 20)
print("\n4. After Deleting '20':")
printLinkedList(my_list_head)