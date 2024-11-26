class Counter:
    def __init__(self):
        self.value = 0
        
    def count_up(self):
        self.value += 1
        
    @property        
    def double_value(self):
        return self.value * 2
    
    @double_value.setter
    def double_value(self, new_value):
        self.value =  new_value // 2
        
        
