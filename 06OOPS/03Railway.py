class RailwayForm:
    # class attribute
    form_type="Railway form"

    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
        print(f"Form is {self.form_type}")




sam=RailwayForm()
# instance attribute
sam.name="sam"
sam.train="Metro"

john=RailwayForm()
john.name="John"
john.train="Rajdhani Express"
# It is now instance attribute of john
john.form_type="RF"
john.printData()
sam.printData()

