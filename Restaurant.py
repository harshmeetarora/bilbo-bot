class Restaurant:
    name = None
    address = None
    priceForTwo = None
    rating = None
    
    def __init__(self, name, address, priceForTwo, rating):
        self.name = name
        self.address = address
        self.priceForTwo = priceForTwo
        self.rating = rating
        
    def printInfo(self):
        print(self.name)
        print(self.address)
        print(self.priceForTwo)
        print(self.rating + "\n")
