class Node ():
    def __init__(self,data):
        self.data = data
        self.next = None
class  LinkedList():
    def __init__(self):
        self.head = None
def PrintList (self):
        temp = self.head
        while temp :
            print (temp.data)
            temp = temp.next


def push(self,new_date) :
    new_node = Node (new_date)
    new_node.next = self.head
    self.head = new_node


def insert (self, prev_node , new_date):
    if prev_node is None :
        print ("Error")
    new_node = Node (new_date)
    new_node.next = prev_node.next
    prev_node.next = new_node

def append (self, new_date):
    new_node = Node (new_date)
    if self.head is None    :
        self.head = new_node
        return
    last = self.head
    while last.next :
        last = last.next
    last.next = new_node

def check(self,data) :
    new_node = Node (data )
    if self.head is None :
        self.head = new_node
        return
    last = self.head
    while last.next:
        if last.next == new_node:
            return last.next
        last = last.next
l_list = LinkedList()
data = []
for i in range(1,20):
    data.append(i)

l_list.head = Node (data[0])
for j in data [1:]:
    l_list.append  (j)

l_list.insert(l_list.check(13),77)
print(l_list.printlist)()




































