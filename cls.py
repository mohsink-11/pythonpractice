class A():
    def __init__(self, a):
        self.a = " This is from class A"
        print("A")
    
class B():
    def __init__(self, b):
        self.b = b
        print("B")

class C(A, B):  
    def __init__(self, a, b):
        A.__init__(self, a)
        B.__init__(self, b)
        self.c = " This is from class C"
        print("This is from the derived class")
    
    def display(self):
        print(self.a, self.b, self.c)

# Example usage
obj = C("A","b") # Create an object of class C 
obj.a = " This is from A" # Set the value of a
obj.display() # Call the display method to show the values of a, b, and c