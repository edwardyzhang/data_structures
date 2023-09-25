#Basic Implementation of a stack in python using lists

class Stack:
    def __init__(self):
        self.values = []
    
    def isEmpty(self):
        return len(self.values) == 0
    
    def pop(self):
        return self.values.pop()
    
    def push(self, value):
        self.values.append(value)

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.values[-1]

#Basic Implementation of a stack using Linked List

#Basic Implementation of a Node
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None
    
    def pop(self):
        if self.top == None:
            return "None"
        else:
            self.top = self.top.next

    def push(self, node):
        if self.top == -1:
            self.top = node
            
        else:
            node.next = self.top
            self.top = node

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.values[-1]
    
    def __str__(self):
        order = ""
        nodes = self.top
        while nodes != None:
            order = order + "->" + str(nodes.value)
            nodes = nodes.next

        return order
        


