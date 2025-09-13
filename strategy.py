# Позволяет менять алгоритм на лету.


class Strategy:
    def execute(self, a, b): pass

class Add(Strategy):
    def execute(self, a, b): return a + b

class Multiply(Strategy):
    def execute(self, a, b): return a * b

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute(self, a, b):
        return self.strategy.execute(a, b)


context = Context(Add())
print(context.execute(2, 3))  # 5
context.set_strategy(Multiply())
print(context.execute(2, 3))  # 6
