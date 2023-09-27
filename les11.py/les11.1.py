class Car:
    def __init__(self, name, kind, model):
        self.name=name
        self.kind=kind
        self.model=model
    
    def start(self):
        print(f"Car:{self.name}, kind: {self.kind}, model: {self.model} is started")
    def stop(self):
        print(f"Car:{self.name}, kind: {self.kind}, model: {self.model} is stopped")
    
car1= Car("BMW", "Car", "X5")
car1.start()