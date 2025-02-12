class User:
    pass # null statement in Python. Nothing happens when it is executed. It is used as a placeholder.


def sleep():
    print("Zzz...")
    pass  

def eat():
    print("Nom nom nom")
    pass


user = User()
user.attribute = "seunan"
user.method = sleep
user.method()

class User:
    def __init__(self, attribute="Default", method=sleep):
        self.attribute = attribute
        self.method = method
        print("Constructor called")

user = User("seunan", eat)
user.method()
