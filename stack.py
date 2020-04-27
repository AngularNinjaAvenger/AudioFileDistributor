class Stack:
     def __init__(self):
         self.store = []

     def isEmpty(self):
         return self.store == []

     def push(self, item):
         self.store.append(item)

     def pop(self):
         return self.store.pop()

     def size(self):
         return len(self.store)