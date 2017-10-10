from author import *
class Book():
    def __init__(self,name,Author,price,qty):
        self.name   =str(name)
        self.authors=Author[self]
        self.price  =float(price)
        self.qty    =int(qty)

    def getName(self):
        return (self.name)

    def getAuthors(self):
        return (self.authors)

    def getPrice(self):
        return (self.price)

    def setPrice(self,amount):
        self.price=amount

    def getQty(self):
        return (self.qty)

    def setQty(self,amount):
        self.qty=amount

    def toString_b(self):
        return("Book :\n"
               "name   ={0}\n"
               "authors={Author[name={1},email={2},gender={3}]}\n"
               "price  ={4}$\n"
               "qty    ={5}"
               .format(self.name,Author.name,Author.email,Author.gender,
                       self.price,self.qty))