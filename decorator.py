# Добавляет новое поведение объекту.


def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

@bold
def hello():
    return "Привет"

print(hello())  # <b>Привет</b>
