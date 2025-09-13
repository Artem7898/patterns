# Пошаговое создание сложного объекта

class Pizza:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        print("Pizza with:", ", ".join(self.parts))


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_cheese(self):
        self.pizza.add("cheese")
        return self

    def add_tomato(self):
        self.pizza.add("tomato")
        return self

    def build(self):
        return self.pizza


pizza = PizzaBuilder().add_cheese().add_tomato().build()
pizza.show()
