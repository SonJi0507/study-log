class Borg:
    __shared_state = {"1": "2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state


b = Borg()
b1 = Borg()
b.x = 4

print("Borg Object 'b' : ", b)
print("Brog Object 'b1': ", b1)
print("Object State 'b':", b.__dict__)
print("Object State 'b1'", b1.__dict__)

"""
Borg Object 'b' :  <__main__.Borg object at 0x105f52230>
Brog Object 'b1':  <__main__.Borg object at 0x105f517b0>
Object State 'b': {'1': '2', 'x': 4}
Object State 'b1' {'1': '2', 'x': 4}
"""


class Borg2(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj
