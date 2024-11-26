class Counter:
    def __init__(self):
        self.value = 0
    def count_up(self):
        self.value += 1
        
class DisplayCounter(Counter):
    def display(self):
        print(f"value = {self.value}")
            
        