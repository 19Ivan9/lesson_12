class Product:
    def __init__(self, category, name, price):
        self.category = category
        self.name = name
        self.price = price
        self.amount = 0
        self.discount = 0


class ProductStore:

    def __init__(self):
        self.products = []

    def add(self, product, amount):
        self.products.append(product)
        product.amount = amount
        print('Added')

    def set_discount(self, identifier_type, percent):
        for prod in self.products:
            if prod.product.name == identifier_type or prod.product.category == identifier_type:
                if prod.product.price < (prod.price * percent / 100):
                    prod.price = (prod.price * percent / 100)

    def sell_product(self, name_product, amount):
        for product in self.products:
            if product.name == name_product and product.amount >= amount:
                product.amount -= amount
                print('Item removed')
            else:
                print('Operation cannot be performed')

    def get_income(self):
        return len(self.products)

    def get_all_products(self):
        products = []
        for product in self.products:
            products.append(
                {
                    'category': product.category,
                    'name': product.name,
                    'price': product.price,
                    'amount': product.amount,
                    'discount': product.discount
                }
            )
            return products

    def get_product_info(self, name_product):
        for product in self.products:
            if product.name == name_product:
                return product.name, product.amount


