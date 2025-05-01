from simple import Home,Room;

class Kitchen(Room,Home):
    def Check2(self):
        print(super()._Names)

        print("_______")
        Room.Check(self)
        print("This is from the Kitchen Class that acces Home",Home.get_Name(self)) 
        print("This is from the Kitchen Class")
    
    def Check(self):
        print("This is from the Second Check Method")

kitchen = Kitchen()
kitchen.Check2()

kitchen.Check()