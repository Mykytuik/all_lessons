class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides =[float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)
    
    def square_rectangle(self):
        square=self.sides[0]*self.sides[1]
        return square
s1=Rectangle()
s1.inputSides()
print(s1.square_rectangle())