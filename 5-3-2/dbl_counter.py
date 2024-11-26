class Counter:
    def __init__(self):
        self.value = 0
    def count_up(self):
        self.value += 1
        
class DoubleCounter(Counter):
    def count_up(self):
        super().count_up()
        super().count_up()
        
                