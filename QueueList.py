class DynamicArray:
    def __init__(self):
        self.list = []
    def popFront(self):
        if not self.list:
            return -1
        return self.list.pop(0) #.pop(index) entfernt und gibt das Element an der angegebenen Position i zurück
    def popLast(self):
        if not self.list:
            return -1
        return self.list.pop() #.pop() entfernt standardnmäßig das letzte Element und gibt das zurück.
    def pushLast(self, i):
        self.list.append(i)
        return i
    def pushFront(self,i):
        self.list.insert(0,i) #.insert setzt den Wert am gewünschten Index in der Liste ein
        return i
    def get (self,i):
        return self.list[i]

test = DynamicArray()

test.pushLast(12)
test.pushLast(45)
test.pushLast(7)
print(test.popFront())
print(test.list)
test.pushLast(34)
test.pushLast(44)
test.pushLast(54)
print(test.list)
test.pushLast(77)
print(test.list)
print(test.get(0))