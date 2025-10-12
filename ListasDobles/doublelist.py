from node import Node

class DoubleList:
    def __init__(self):
        self._head = None
        self._lastnode = None

    
    def add(self, n):
        if self._head is None:
            self._head = n
            self._lastnode = n  
            return

        if n.data < self._head.data:
            n.next = self._head
            self._head.back = n
            self._head = n
            return

        h = self._head
        while h.next is not None:
            if n.data < h.next.data:
                n.next = h.next
                n.back = h
                h.next = n
                n.next.back = n
                return
            h = h.next

        h.next = n
        n.back = h
        self._lastnode = n  


    def remove(self, data):
        current = self._head

        while current is not None:
            if current.data == data:
                if current.back is not None:
                    current.back.next = current.next
                else:
                    self._head = current.next
                if current.next is not None:
                    current.next.back = current.back
                else:
                    self._lastnode = current.back
                return 
            current = current.next

    def exists(self, data):
        h = self._head
        while h is not None:
            if h.data == data:
                return True
            if data < h.data:
                return False
            h = h.next
        return False

    def count(self):
        count = 0
        h = self._head
        while h is not None:
            count += 1
            h = h.next
        return count

    def show(self):
        if self._head is None:
            return "Empty List"
        i = 0
        h = self._head
        datas = ""
        while h is not None:
            datas += f"Node [{i}] and: {h}\n"
            i += 1
            h = h.next
        return datas

    def reverse_show(self):
        if self._head is None:
            return "Empty List"
        l = self._lastnode
        i = 0
        datas = ""
        while l is not None:
            datas += f"Node [{i}] and {l}\n"
            l = l.back
            i += 1
        return datas

    def clear(self):
        self._head = None
        self._lastnode = None

    def __str__(self):
        result = ""
        h = self._head
        while h is not None:
            result += str(h) + "\n"
            h = h.next
        return result