class History:
    def __init__(self, product_name, qty, price, date, time):
        self.name = product_name
        self.quantity = qty
        self.price = price
        self.date = date
        self.time = time

    def format_for_file(self):
        return f"{self.date},{self.time},{self.name},{self.quantity},{self.price}\n"
