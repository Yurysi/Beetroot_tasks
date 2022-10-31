class Products:
    def __init__(self, product_type, name, price):
        self.product_type = product_type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.income = 0
        self.products = dict()

    def add(self, product, amount):
        try:
            if product.name in self.products:
                self.products[product.name]["amount"] += amount
            else:
                self.products[product.name] = {
                    "price": product.price,
                    "store price": product.price * 1.3,
                    "amount": amount,
                    "product_type": product.product_type
                }
            return self.products
        except Exception:
            raise ValueError("Cant add this product")

    def set_discount(self, identifier, percent, identifier_type="name"):
        if any(identifier in item.values() for item in self.products.values()):
            self.set_discount_by_type(identifier, percent)
        elif identifier_type == "name":
            self.set_discount_by_name(identifier, percent)
        else:
            raise ValueError("Cant set the discount")
        return self.products

    def set_discount_by_name(self, identifier, percent):

        if self.products.get(identifier):
            self.products[identifier]["store price"] = self.products[identifier]["store price"] * (
                    1 - (int(percent)) / 100)
        else:
            raise ValueError('Cant set this discount')
        return self.products

    def set_discount_by_type(self, identifier, percent):
        for key, value in self.products.items():
            if value["product_type"] == identifier:
                self.products[key]["store price"] = self.products[key]["store price"] * (1 - (int(percent)) / 100)
            else:
                raise ValueError('No such product type')
            return self.products

    def check_by_name(self, product):
        if product in self.products:
            return True
        return False

    def check_by_amount(self, product, amount):
        if self.products.get(product).get("amount") >= amount:
            return True
        return False

    def sell_product(self, product, amount):
        if self.check_by_name(product):
            if self.check_by_amount(product, amount):
                self.products[product]["amount"] -= amount
                self.income += round(((self.products[product]["store price"] - self.products[product]["price"]) * amount), 2)
            else:
                raise ValueError('No such product')
        return self.products

    def get_income(self):
        return f"Store income is {self.income}"

    def get_all_products(self):
        return [key for key in self.products.keys()]

    def get_product_info(self, name):
        if self.check_by_name(name):
            return name, self.products[name]["amount"]
        else:
            return f"There is no such product as '{name}' in our store"




shop1 = ProductStore()
product1 = Products("fruits", "orange", 20)
product2 = Products("fruits", "apple", 10)
print(shop1.add(product1, 5))
print(shop1.add(product2, 20))
print(shop1.set_discount("fruits", 20))
print(shop1.sell_product("orange", 999))
print(shop1.get_income())
print(shop1.get_all_products())
print(shop1.get_product_info("oran"))