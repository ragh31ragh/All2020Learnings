"""Stack DataStructure"""

class Stack():
    def __init__(self):
        self.items = [];
        print("Executing constructor")
    def push(self,item):
        self.items.append(item)
        print("Executing push method")
    def pop(self):
        return self.items.pop()
    def getstack(self):
        return self.items

s=Stack()
s.push('A')
s.push('B')
s.push('C')
print(s.getstack())
s.pop()
print(s.getstack())