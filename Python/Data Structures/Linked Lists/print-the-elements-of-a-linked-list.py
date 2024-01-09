

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

## Iterative solution
def printLinkedList(head):
    while head is not None:
        print(head.data)
        head = head.next


## Recursive solution
def printLinkedList2(head):
    if head:
        print(head.data)
        printLinkedList2(head.next)


