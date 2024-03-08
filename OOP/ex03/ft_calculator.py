class calculator:
    """"""
    def __init__(self, object):
        """"""
        self.obj = object

    def __add__(self, object) -> None:
        """"""
        self.obj = [x + object for x in self.obj]
        print(self.obj)

    def __mul__(self, object) -> None:
        """"""
        self.obj = [x * object for x in self.obj]
        print(self.obj)

    def __sub__(self, object) -> None:
        """"""
        self.obj = [x - object for x in self.obj]
        print(self.obj)

    def __truediv__(self, object) -> None:
        """"""
        self.obj = [x / object for x in self.obj]
        print(self.obj)
