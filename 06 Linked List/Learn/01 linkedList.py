

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

head = node1
node1.next = node2
node2.next = node3


class LinkedList:
    def __init__(self, data) -> None:
        self.head = Node(data)

    def insertEnd(self, data) -> None:
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(data)

    def insertBegin(self, data) -> None:
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead

    def searchNode(self, data) -> int:
        temp = self.head
        index = 0
        while temp != None:
            if temp.data == data:
                return index
            else:
                temp = temp.next
                index += 1
        return -1

    def insertAt(self, data, index) -> None:
        temp = self.head
        newNode = Node(data)
        if temp.next == None:
            if index == 1:
                temp.next = newNode
            return

        temp2 = temp.next
        currIndex = 1
        while temp2 != None:
            if currIndex == index:
                temp.next = newNode
                newNode.next = temp2
                return
            else:
                temp = temp2
                temp2 = temp2.next
                currIndex += 1

    def printList(self) -> None:
        temp = self.head
        while temp != None:
            print(temp.data, end=" -> ")
            temp = temp.next


linkedList = LinkedList(10)
linkedList.insertEnd(20)
linkedList.insertEnd(30)
linkedList.insertEnd(40)
linkedList.insertBegin(9)
linkedList.insertBegin(8)
linkedList.insertBegin(7)
linkedList.insertBegin(6)
linkedList.insertBegin(5)

linkedList.printList()

print("\n\nSearching")

print("Index of 5   : " + str(linkedList.searchNode(5)))
print("Index of 40  : " + str(linkedList.searchNode(40)))
print("Index of 6   : " + str(linkedList.searchNode(6)))
print("Index of 30  : " + str(linkedList.searchNode(30)))
print("Index of 10  : " + str(linkedList.searchNode(10)))
print("Index of 100 : " + str(linkedList.searchNode(100)))

print("\n\nInsertion")
# linkedList.insertAt(1, 0)
# linkedList.printList()
# print("\n")

# linkedList.insertAt(100, 9)
# linkedList.printList()
# print("\n")

linkedList.insertAt(12, 5)
linkedList.printList()
print("\n")
