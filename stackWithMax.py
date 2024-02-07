class Stack:
    def __init__(self):
        self.items = []
        self.max_items = []
        
    def push(self, val):
        self.items.append(val)
        if not self.max_items or val >= self.max_items[-1]:
            self.max_items.append(val)
    
    def pop(self):
        if not self.items:
            return None
        val = self.items.pop()
        if val == self.max_items[-1]:
            self.max_items.pop()
        return val
    
    def max(self):
        if not self.max_items:
            return None
        return self.max_items[-1]

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.max()) # Output: 3
stack.pop()
print(stack.max()) # Output: 2
stack.push(4)
print(stack.max()) # Output: 4
stack.pop()
stack.pop()
print(stack.max()) # Output: 1
stack.pop()
print(stack.max()) # Output: None
