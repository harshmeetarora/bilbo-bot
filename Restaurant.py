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
        output = ""
        output += "Name: " + self.name + "\n"
        output += "Address: " + self.address + "\n"
        output += "Average price for two: " + self.priceForTwo + "\n"
        output += "Rating: " + self.rating + "\n"
        return output