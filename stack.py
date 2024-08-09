from linkedlist import LinkedList

class Stack:
    def __init__(self):
        self.list = LinkedList()
    
    def push(self, obj):
        """
        Push an object onto the top of the stack

        Parameters
        ----------
        obj: object
            Object to push on
        """
        ## TODO: Fill this in
    
    def pop(self):
        """
        Pop the object from the top of the stack, or
        return None if the stack is empty

        Returns
        -------
        object:
            Object at the top of the list
        """
        ret = None
        ## TODO: Fill this in
        return ret
    

def __init__(self):
    s = Stack()
    s.push("A")
    s.push("B")
    s.push("C")
    for i in range(3):
        print(s.pop())