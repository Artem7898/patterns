# Контролирует доступ к объекту.


class RealSubject:
    def request(self):
        print("Выполнение запроса")

class Proxy:
    def __init__(self, real):
        self.real = real

    def request(self):
        print("Проверка прав")
        self.real.request()

proxy = Proxy(RealSubject())
proxy.request()
