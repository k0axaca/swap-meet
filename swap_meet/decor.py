from swap_meet.item import Item

class Decor(Item):
    def __init__(self, category = "", condition = 0):
        super().__init__(category = "", condition = 0)
        self.condition = condition
        self.category = "Decor"

    def __str__(self):
        return "Something to decorate your space."

 
        

