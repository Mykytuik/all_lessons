class Human():
    def __init__(self, name) -> None:
        self.name=name
    def hello(self):
        print(f"Hello {self.name}")
    @classmethod
    def classmethod(cls):
        print("Homosapiens")
    @staticmethod
    def staticmethod():
        print("Static method")

Human_Bob=Human("Bob")
Human_Bob.hello()
Human_Bob.classmethod()
Human_Bob.staticmethod()