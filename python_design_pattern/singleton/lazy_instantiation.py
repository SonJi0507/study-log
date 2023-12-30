class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called..")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton()
print("Object created", Singleton.getInstance())
s1 = Singleton()

"""
__init__ method called..
__init__ method called..
Object created <__main__.Singleton object at 0x106174580>
Instance already created: <__main__.Singleton object at 0x106174580>
"""
