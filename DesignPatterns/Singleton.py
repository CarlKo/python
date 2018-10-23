""" ref. https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm """
class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()

            return Singleton.__instance
    
s = Singleton()
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s)
