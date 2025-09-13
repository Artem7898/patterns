# Оповещает подписчиков об изменениях.


class Observer:
    def update(self, message): pass

class User(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} получил: {message}")

class Chat:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, user):
        self.subscribers.append(user)

    def notify(self, msg):
        for sub in self.subscribers:
            sub.update(msg)


chat = Chat()
u1 = User("Артем")
u2 = User("Вася")
chat.subscribe(u1)
chat.subscribe(u2)

chat.notify("Новая новость!")
