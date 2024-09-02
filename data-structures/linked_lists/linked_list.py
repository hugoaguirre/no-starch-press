"""
    Linked list implementation

    Insert, delete and update nodes
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head: int):
        self.head = Node(head)

    def insert(self, value: int, index: int):
        """ Inserts node at position `index` """
        if index == 0:
            tmp = self.head
            new_head = Node(value)
            self.head = new_head
            self.head.next = tmp
            return index

        previous = None
        current = self.head
        count = 0
        while count < index and current != None:
            previous = current
            current = current.next
            count += 1

        if count < index:
            printf("Invalid index provided")
            return

        new_node = Node(value)
        previous.next = new_node
        new_node.next = current

    def append(self, value: int):
        """ Inserts node at the end of the list """
        previous = None
        current = self.head

        while current != None:
            previous = current
            current = current.next

        previous.next = Node(value)

    def removeItem(self, value: int):
        """ Removes the first `value` encounter from the list """
        previous = None
        current = self.head

        if self.head.value == value:
            tmp = self.head
            self.head = tmp.next
            return

        while current != None and current.value != value:
            previous = current
            current = current.next

        if current is None:
            print("unable to remove: not found")
            return

        previous.next = current.next
        current.next = None

    def remove(self, index: int):
        """ Removes the value from the list at position `index` """
        previous = None
        current = self.head

        if index == 0:
            tmp = self.head
            self.head = tmp.next
            return

        previous = None
        current = self.head
        count = 0
        while current != None and count < index:
            previous = current
            current = current.next
            count += 1

        if count < index:
            print("unable to remove: not found")
            return

        previous.next = current.next
        current.next = None

    def pprint(self):
        """ Pretty prints the linked list nodes """
        current = self.head
        output = ""

        if self.head is None:
            return

        if current.next is None:
            print(current.value)
            return

        while current != None:
            if current.next != None:
                output += f"{current.value} --> "
            else:
                output += f"{current.value}"
            current = current.next
        print(output)

if __name__ == "__main__":
    ll = LinkedList(3)
    ll.insert(54, 0)
    ll.insert(99, 0)

    ll.insert(82, 1)
    ll.insert(85, 1)

    ll.append(100)
    ll.append(44)

    ll.removeItem(100)
    ll.removeItem(99)

    ll.remove(1)
    ll.remove(3)
    ll.remove(0)
    ll.remove(0)
    ll.remove(0)
    ll.pprint()
