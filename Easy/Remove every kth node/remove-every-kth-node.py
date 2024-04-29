#Your task is to complete this function
#Your function should return the new head pointer
'''
class node:
    def __init__(self,x):
        self.data = x
        self.next = None
'''

class Solution:
    def deleteK(self, head, k):
        #code here
        # Edge case: if head is None or k is less than or equal to 0, return None
        if not head or k <= 0:
            return None
    
        # Initialize two pointers, prev and curr, to traverse the linked list
        prev = None
        curr = head
        count = 0
    
        # Traverse the linked list
        while curr:
            count += 1
            # If count is equal to k, remove the current node
            if count == k:
                # If the node to be removed is the head, update head
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
                count = 0  # Reset count after removal
            else:
                # Move prev and curr pointers forward
                prev = curr
            curr = curr.next
    
        return head
                


#{ 
 # Driver Code Starts
class node:

    def __init__(self, x):
        self.data = x
        self.next = None


def createLinkedList(arr):
    head = node(arr[0])
    curr = head
    for i in range(1, len(arr)):
        new_node = node(arr[i])
        curr.next = new_node
        curr = curr.next

    return head


def printlist(ptr):
    while ptr != None:
        print(ptr.data, end=" ")
        ptr = ptr.next
    print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())

        obj = Solution()
        head = createLinkedList(arr)
        new_head = obj.deleteK(head, k)
        printlist(new_head)

# } Driver Code Ends