class Car:
    def __init__(self, model, company, price):
        self.__model = model
        self.__company = company
        self.__price = price

    def show_details(self):
        print(f"Model: {self.__model}, Company: {self.__company}, Price: {self.__price}")

car1 = Car("Mustang", "Ford", 6000000)
car1.show_details()
print(car1.__dict__)
    