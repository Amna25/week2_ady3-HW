class Customer:
    def __init__(self, name, wallet):
        self.name= name
        self.stomach= []
        self.wallet= wallet

    def customer_buy_drink(self, amount):
        self.wallet -=  amount
        
    
