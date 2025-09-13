# Позволяет объектам с разными интерфейсами работать вместе.


class OldPrinter:
    def print_old(self):
        print("Старый принтер")

class NewPrinter:
    def print_new(self):
        print("Новый принтер")

class Adapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print_new(self):
        self.old_printer.print_old()

printer = Adapter(OldPrinter())
printer.print_new()  # Старый принтер
