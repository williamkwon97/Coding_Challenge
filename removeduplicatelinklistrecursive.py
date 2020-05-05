# Python3 Program to remove duplicates 
# from a sorted linked list  
import math 
  
# Link list node  
class Node:  
    def __init__(self,data):  
        self.data = data  
        self.next = None
  
# The function removes duplicates  
# from a sorted list  
def removeDuplicates(head):  
      
    # Pointer to store the pointer of a node  
    # to be deleted to_free  
      
    # do nothing if the list is empty  
    if (head == None):  
        return
  
    # Traverse the list till last node  
    if (head.next != None):  
          
        # Compare head node with next node  
        if (head.data == head.next.data):  
              
            # The sequence of steps is important.  
            # to_free pointer stores the next of head  
            # pointer which is to be deleted.  
            to_free = head.next
            head.next = head.next.next
              
            # free(to_free)  
            removeDuplicates(head)  
          
        # This is tricky: only advance if no deletion 
        else:  
            removeDuplicates(head.next)  
          
    return head 
  
# UTILITY FUNCTIONS  
# Function to insert a node at the  
# beginging of the linked list  
def push(head_ref, new_data):  
      
    # allocate node  
    new_node = Node(new_data)  
              
    # put in the data  
    new_node.data = new_data  
                  
    # link the old list off the new node  
    new_node.next = head_ref      
          
    # move the head to point to the new node  
    head_ref = new_node 
    return head_ref 
  
# Function to print nodes in a given linked list  
def printList(node):  
    while (node != None):  
        print(node.data, end = " ")  
        node = node.next
      
# Driver code 
if __name__=='__main__':  
  
    # Start with the empty list  
    head = None
      
    # Let us create a sorted linked list 
    # to test the functions  
    # Created linked list will be 11.11.11.13.13.20  
    head = push(head, 20)  
    head = push(head, 13)  
    head = push(head, 13)  
    head = push(head, 11)  
    head = push(head, 11)  
    head = push(head, 11)                                  
  
    print("Linked list before duplicate removal ", 
                                         end = "")  
    printList(head)  
  
    # Remove duplicates from linked list  
    removeDuplicates(head)  
  
    print("\nLinked list after duplicate removal ", 
                                          end = "")  
    printList(head)          
      