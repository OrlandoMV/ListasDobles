from node import Node

class DoubleList:
    def __init__(self):
        self._head = None

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = value

    def add(self, n: Node):
        if self._head is None:
            self._head = n
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
                h.next.back = n
                h.next = n
                return
            h = h.next

        h.next = n
        n.back = h

    def remove(self, data: int):
        if self._head is None:
            return

        if self._head.data == data:
            if self._head.next is not None:
                self._head.next.back = None
            self._head = self._head.next
            return

        h = self._head
        while h.next is not None:
            if h.next.data == data:
                temp = h.next
                h.next = temp.next
                if temp.next is not None:
                    temp.next.back = h
                return
            h = h.next

    def exists(self, data: int) -> bool:
        h = self._head
        while h is not None:
            if h.data == data:
                return True
            h = h.next
        return False

    def count(self) -> int:
        count = 0
        h = self._head
        while h is not None:
            count += 1
            h = h.next
        return count

    def show(self) -> str:
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

    def reverse_show(self) -> str:
        if self._head is None:
            return "Empty List"

        h = self._head
        last = None
        i = 0
        while h is not None:
            last = h
            h = h.next
            i += 1

        datas = ""
        i -= 1
        h = last
        while h is not None:
            datas += f"Node [{i}] {h}\n"
            h = h.back
            i -= 1
        return datas

    def clear(self):
        self._head = None

    def __str__(self):
        result = ""
        h = self._head
        while h is not None:
            result += str(h) + "\n"
            h = h.next
        return result
