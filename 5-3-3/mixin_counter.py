class Counter:
    def __init__(self):
        self.value = 0
    def count_up(self):
        self.value += 1
        
class DisplayValue:
    def display(self):
        print(f"value is {self.value}") 
        
class DisplayCounter(Counter, DisplayValue):
    pass                    