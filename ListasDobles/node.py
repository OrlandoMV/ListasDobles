class Node:
    def __init__(self, data):
        self._data = data
        self._next = None
        self._back = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value

    @property
    def back(self):
        return self._back

    @back.setter
    def back(self, value):
        self._back = value

    def __str__(self):
        return f"Data: {self._data}"

