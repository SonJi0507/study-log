class MyInt(type):
    def __call__(cls, *args, **kwds):
        print(" === Here's My int === ")
        print("Now do whatever you want with these objects...")
        return type.__call__(cls, *args, **kwds)
    
class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y

i = int(4, 5)
"""
int class 생성시 MyInt의 __call__ 가 실행 됨. 객체 생성을 metaclass가 제어함
"""