from datetime import datetime

class Chore:
    name = ''
    dateComplete = datetime.now()
    frequency = 0 ##how often a chore is to be completed 
    priority = 0
    
    def __init__(self, n, f, d):
        self.name = n
        self.dateComplete = datetime.strptime(d, '%m-%d-%Y').date()
        self.frequency = int(f)
        elapsed = (datetime.now().date() - self.dateComplete).days
        if elapsed > self.frequency:
            self.priority = elapsed - self.frequency
            