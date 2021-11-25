class Pub:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash  


    def increase_cash(self, amount):
        self.cash +=  amount