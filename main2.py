class Book:
    def set_price(self, val):
        self._price = val + 1

    def get_price(self):
        return self._price + 1
    
obj = Book()
obj.set_price(15)
print(obj.get_price())