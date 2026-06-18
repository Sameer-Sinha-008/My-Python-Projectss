
class Rectangle:
    
    
    def __init__(self, Length, Width):
        self.Length = Length
        self.Width = Width
        
    def area(self):
        result = self.Length * self.Width
        print(f"Their area is {result}")

my_reactangle = Rectangle(10, 5)
my_reactangle.area() 
