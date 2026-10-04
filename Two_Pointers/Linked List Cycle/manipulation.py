class LinkedList(object):
    def __init__(self,x):
        self.val=x # stores the value you pass in
        self.next=None # no next yet 

# how to create a linkedlist : 1->2->3->None

a=LinkedList(1)
b=LinkedList(2)
c=LinkedList(3)

a.next=b
b.next=c

head=a
parts=[]
while head:
    parts.append(head.val)
    head=head.next
print(parts)

# if u want to prent the linked list in this format 1->2->3->None

print(" Another way to print:")

parts1=[]
node=a
while node:
    parts1.append(str(node.val))# this because the join method operate on the string type object 
    node=node.next
parts1.append("None")
print("->".join(parts1))

# a function that print a  linked list in this way !!

def print_ll(head):
    list=[]
    node=head
    while node:
        list.append(str(node.val))
        node=node.next
    list.append("None")
    return "->".join(list)
print(print_ll(a))