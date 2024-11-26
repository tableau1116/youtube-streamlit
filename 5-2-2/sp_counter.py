class Counter:
    def __init__(self, initial=0):
        self.value = initial
        
    def count_up(self) :
        self.value += 1
        
    def __str__(self):
        return f"Counter({self.value})"
    
    def __add__(self, other):
        return Counter(self.value + other.value)       
    