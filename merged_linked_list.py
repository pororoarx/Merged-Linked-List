# Create a class named ListNode
class ListNode:
    def __init__(self, value=0, next=None):
        # Initialize the node's value attribute
        self.value = value
        # Initialize the 'next' attribute for the next node
        self.next = next
        
# Merge the two sorted linked lists
def merge_sorted_list(list1, list2):
    # Initialize the pointers
    result = ListNode (-1) # dummy node
    current = result

    # Loop through both lists
    while list1 is not None and list2 is not None:
        # Compare the values of the nodes for each list. If list1 is less than list2, set the least value as the next node.
        if list1.value < list2.value:
            # Set the value of the current node in the merged linked list with the value of the node in list1
            current.next = list1
            # Move the pointer to the next node in list1
            list1 = list1.next
        # Else, if list2 is less than list1, set the least value as the next node.
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Handle all the remaining nodes in list1
    while list1 is not None:
        current.next = list1
        list1 = list1.next
        current = current.next

    # Handle all the remaining nodes in list 2
    while list2 is not None:
        current.next = list2
        list2 = list2.next
        current = current.next

    # skip the dummy node
    return result.next

# Ask user for input (integers separated by space) and create a sorted linked list
def input_linked_list():
    input_list = input("Enter elements separated by space: ")
    # Converts the input string into a list of integers
    elements = list(map(int, input_list.split()))

    # Check if the number of nodes is within the range [0, 50]
    if not (0 <= len(elements) <= 50):
        print("Error. The number of nodes should be within the range 0-50 only.")
        return None
    
    # Check if the value of nodes are within the range [0, 100]
    for element in elements:
        if not (-100 <= element <= 100):
            print("Error. The node value should be within the range 0-100 only.")
            return None
        
    # Sort the elements in non-decreasing order
    elements.sort()

    result = ListNode(-1)
    current = result

    # Create nodes with sorted values and append them to the result list
    for element in elements:
        current.next = ListNode(element)
        current = current.next

    return result.next

# Take the user input for list1
print("\n>>> Enter elements for the first linked list")
list1 = input_linked_list()

# Take the user input for list1
print("\n>>> Enter elements for the second linked list")
list2 = input_linked_list()

# Check list1 and list2 if empty
if list1 is not None and list2 is not None:
    # Print the user's input for list1
    print("\nList 1: ", end="")
    current = list1
    while current:
        # Print the value of the current node
        print(current.value, end="")
        # Then the next node
        current = current.next
        # If there is a next node, print an arrow symbol
        if current:
            print(" -> ", end="")
    print()

    # Print the user's input for list2
    print("List 2: ", end="")
    current = list2
    while current:
        # Print the value of the current node
        print(current.value, end="")
        # Then the next node
        current = current.next
        # If there is a next node, print an arrow symbol
        if current:
            print(" -> ", end="")
    print()

    # Merge the lists and print the merged list
    merged_list = merge_sorted_list(list1, list2)
    print("\nMerged Linked List:", end=" ")
    current = merged_list
    while current:
        # Print the value of the current node
        print(current.value, end="")
        # Then the next node
        current = current.next
        # If there is a next node, print an arrow symbol
        if current:
            print(" -> ", end="")
    print()