# Паттерны проектирования в Python 3:  23 классическими паттернами GoF на Python 3


## 📌 Что такое паттерны проектирования
**Паттерн проектирования (design pattern)** — это готовое решение часто встречающейся задачи проектирования.
Это не конкретный код, а **шаблон**, который можно адаптировать под нужды проекта.

Они помогают:
- писать более **читаемый и поддерживаемый код**;
- **избегать дублирования логики**;
- **ускорять разработку** за счёт готовых решений;
- упрощать **командную работу** (разработчики понимают паттерн сразу).

---

## 🔹 Основные группы паттернов
1. **Порождающие (Creational)** — отвечают за создание объектов.
2. **Структурные (Structural)** — описывают, как компоненты программы связаны между собой.
3. **Поведенческие (Behavioral)** — описывают взаимодействие между объектами.

---

Полный справочник по **классическим паттернам GoF** с краткой теорией, когда применять, плюс-минусами и **минимальными Python‑примерами**. Акцент на «питоничных» приёмах: протоколы, утиную типизацию, функции высшего порядка, dataclasses.

> Python 3.x, без сторонних библиотек. Примеры лаконичны, чтобы было легко перенести в рабочий код.

---

## Содержание
- [Порождающие](#порождающие)
  - [Singleton](#singleton-одиночка)
  - [Factory Method](#factory-method-фабричный-метод)
  - [Abstract Factory](#abstract-factory-абстрактная-фабрика)
  - [Builder](#builder-строитель)
  - [Prototype](#prototype-прототип)
- [Структурные](#структурные)
  - [Adapter](#adapter-адаптер)
  - [Bridge](#bridge-мост)
  - [Composite](#composite-компоновщик)
  - [Decorator](#decorator-декоратор)
  - [Facade](#facade-фасад)
  - [Flyweight](#flyweight-легковес)
  - [Proxy](#proxy-заместитель)
- [Поведенческие](#поведенческие)
  - [Chain of Responsibility](#chain-of-responsibility-цепочка-обязанностей)
  - [Command](#command-команда)
  - [Interpreter](#interpreter-интерпретатор)
  - [Iterator](#iterator-итератор)
  - [Mediator](#mediator-посредник)
  - [Memento](#memento-хранитель)
  - [Observer](#observer-наблюдатель)
  - [State](#state-состояние)
  - [Strategy](#strategy-стратегия)
  - [Template Method](#template-method-шаблонный-метод)
  - [Visitor](#visitor-посетитель)

---

## Порождающие

### Singleton (Одиночка)
**Идея:** один экземпляр и глобальная точка доступа.  
**Когда:** конфигурация, логгер, пул соединений.  
**Плюсы:** контроль единственности. **Минусы:** скрытая глобальность, сложно тестировать.

```python
class Singleton:
    _inst = None
    def __new__(cls, *a, **k):
        if not cls._inst:
            cls._inst = super().__new__(cls)
        return cls._inst
```

> Питонично: использовать модуль как синглтон или `functools.lru_cache` на фабрике.

---

### Factory Method (Фабричный метод)
**Идея:** делегировать создание подклассам.  
**Когда:** варианты продуктов, инверсия зависимостей.

```python
class Button: 
    def render(self): ...

class WinButton(Button):
    def render(self): print("Win")

class LinuxButton(Button):
    def render(self): print("Linux")

class Dialog:
    def create_button(self) -> Button: ...
    def render(self):
        btn = self.create_button()
        btn.render()

class WinDialog(Dialog):
    def create_button(self): return WinButton()

class LinuxDialog(Dialog):
    def create_button(self): return LinuxButton()
```

---

### Abstract Factory (Абстрактная фабрика)
**Идея:** создавать **семейства** связанных объектов без привязки к конкретным классам.  
**Когда:** кроссплатформенные наборы UI, драйверы.

```python
class CheckBox: ...
class Button: ...

class WinCheckBox(CheckBox): ...
class WinButton(Button): ...
class LinuxCheckBox(CheckBox): ...
class LinuxButton(Button): ...

class GUIFactory:
    def create_button(self) -> Button: ...
    def create_checkbox(self) -> CheckBox: ...

class WinFactory(GUIFactory):
    def create_button(self): return WinButton()
    def create_checkbox(self): return WinCheckBox()

class LinuxFactory(GUIFactory):
    def create_button(self): return LinuxButton()
    def create_checkbox(self): return LinuxCheckBox()
```

---

### Builder (Строитель)
**Идея:** пошаговая сборка сложного объекта.  
**Когда:** много опциональных параметров/вариантов.

```python
class Report:
    def __init__(self): self.parts = []
    def add(self, x): self.parts.append(x)

class ReportBuilder:
    def __init__(self): self.r = Report()
    def header(self, t): self.r.add(("header", t)); return self
    def table(self, rows): self.r.add(("table", rows)); return self
    def build(self): return self.r

rep = ReportBuilder().header("Sales").table([1,2,3]).build()
```

---

### Prototype (Прототип)
**Идея:** копировать объекты вместо создания с нуля.  
**Когда:** дорого инициализировать, нужна частичная копия.

```python
import copy

class Node:
    def __init__(self, v, meta=None):
        self.v, self.meta = v, (meta or {})
    def clone(self):
        return copy.deepcopy(self)

a = Node(1, {"tags": ["hot"]})
b = a.clone()
```

---

## Структурные

### Adapter (Адаптер)
**Идея:** согласовать несовместимые интерфейсы.  
**Когда:** обёртка над Legacy/внешним API.

```python
class OldPrinter:
    def print_old(self): print("old")

class NewIface:
    def print(self): ...

class Adapter(NewIface):
    def __init__(self, old): self.old = old
    def print(self): self.old.print_old()
```

---

### Bridge (Мост)
**Идея:** разделить абстракцию и реализацию, чтобы менять независимо.  
**Когда:** комбинации платформ/движков/рендеров.

```python
class Renderer:
    def render_circle(self, x, y, r): ...

class VectorRenderer(Renderer):
    def render_circle(self, x,y,r): print("vector circle")

class RasterRenderer(Renderer):
    def render_circle(self, x,y,r): print("raster circle")

class Circle:
    def __init__(self, renderer, x,y,r):
        self.rnd, self.x, self.y, self.r = renderer, x, y, r
    def draw(self): self.rnd.render_circle(self.x, self.y, self.r)
```

---

### Composite (Компоновщик)
**Идея:** дерево «часть‑целое», единый интерфейс для листьев и контейнеров.  
**Когда:** иерархии UI/файловые системы/сцены.

```python
class Component:
    def render(self): ...

class Text(Component):
    def __init__(self, t): self.t = t
    def render(self): print(self.t)

class Panel(Component):
    def __init__(self): self.children = []
    def add(self, c): self.children.append(c)
    def render(self):
        for c in self.children: c.render()

root = Panel(); root.add(Text("Hello")); root.render()
```

---

### Decorator (Декоратор)
**Идея:** динамически расширять поведение без наследования.  
**Когда:** логирование, кеш, ретраи, авторизация.

```python
def logged(fn):
    def wrapper(*a, **k):
        print("call", fn.__name__)
        return fn(*a, **k)
    return wrapper

@logged
def calc(x, y): return x + y
```

---

### Facade (Фасад)
**Идея:** единая простая точка входа к сложной подсистеме.  
**Когда:** сокрытие деталей, удобный API.

```python
class VideoDecoder: ...
class AudioDecoder: ...
class Player:
    def play(self, path):
        VideoDecoder(); AudioDecoder()
        print("Playing", path)
```

---

### Flyweight (Легковес)
**Идея:** разделять неизменяемое состояние между множеством объектов.  
**Когда:** много мелких однотипных объектов (символы, частицы).

```python
class GlyphFactory:
    _pool = {}
    def get(self, char):
        if char not in self._pool:
            self._pool[char] = object()  # разделяемый «вес»
        return self._pool[char]

f = GlyphFactory()
a1, a2 = f.get('a'), f.get('a')
assert a1 is a2
```

---

### Proxy (Заместитель)
**Идея:** контролировать доступ, лениво инициализировать, добавлять кросс‑срезы.  
**Когда:** lazy‑load, кеш, контроль прав, удалённые объекты.

```python
class Service:
    def data(self): print("real data")

class ServiceProxy:
    def __init__(self, real): self.real = real
    def data(self):
        print("auth check")
        return self.real.data()

ServiceProxy(Service()).data()
```

---

## Поведенческие

### Chain of Responsibility (Цепочка обязанностей)
**Идея:** передавать запрос по цепочке обработчиков.  
**Когда:** фильтры, middleware, валидации.

```python
class Handler:
    def __init__(self, nxt=None): self.nxt = nxt
    def handle(self, req):
        if self.nxt: return self.nxt.handle(req)

class Auth(Handler):
    def handle(self, req):
        if not req.get("user"): return "401"
        return super().handle(req)

class Validate(Handler):
    def handle(self, req):
        if "payload" not in req: return "400"
        return super().handle(req)

pipe = Auth(Validate())
print(pipe.handle({"user": "u", "payload": 1}))  # None => ok
```

---

### Command (Команда)
**Идея:** инкапсуляция действия в объект; поддержка undo/redo, очередей.  
**Когда:** GUI-кнопки, макросы, таск‑кью.

```python
class Command:
    def execute(self): ...
    def undo(self): ...

class AddText(Command):
    def __init__(self, buf, txt): self.buf, self.txt = buf, txt
    def execute(self): self.buf.append(self.txt)
    def undo(self): self.buf.pop()

buf = []
cmd = AddText(buf, "hi"); cmd.execute(); cmd.undo()
```

---

### Interpreter (Интерпретатор)
**Идея:** язык + грамматика + интерпретация выражений.  
**Когда:** простые DSL, фильтры, правила.

```python
class Num: 
    def __init__(self, v): self.v = v
    def eval(self): return self.v

class Add:
    def __init__(self, l, r): self.l, self.r = l, r
    def eval(self): return self.l.eval() + self.r.eval()

expr = Add(Num(2), Add(Num(3), Num(4)))
print(expr.eval())  # 9
```

---

### Iterator (Итератор)
**Идея:** единый интерфейс обхода коллекции.  
**Когда:** скрыть устройство коллекции, ленивые последовательности.

```python
class Range:
    def __init__(self, n): self.n = n
    def __iter__(self):
        i = 0
        while i < self.n:
            yield i
            i += 1

for x in Range(3): pass
```

> В Python есть генераторы, `itertools`, comprehensions — зачастую достаточно их.

---

### Mediator (Посредник)
**Идея:** координация взаимодействия между объектами через посредника.  
**Когда:** сложные взаимосвязи виджетов, чатов, модулей.

```python
class Chat:
    def __init__(self): self.users = []
    def join(self, u): self.users.append(u); u.chat = self
    def send(self, from_, msg):
        for u in self.users:
            if u is not from_: u.recv(msg)

class User:
    def __init__(self, name): self.name = name; self.chat=None
    def send(self, msg): self.chat.send(self, f"{self.name}: {msg}")
    def recv(self, msg): print(msg)
```

---

### Memento (Хранитель)
**Идея:** сохранять/восстанавливать состояние без раскрытия внутренностей.  
**Когда:** undo/redo, снапшоты.

```python
class Editor:
    def __init__(self): self.text = ""
    def save(self): return self.text[:]          # memento
    def restore(self, m): self.text = m

e = Editor(); e.text="a"; m=e.save(); e.text="b"; e.restore(m)
```

---

### Observer (Наблюдатель)
**Идея:** подписчики получают уведомления об изменениях.  
**Когда:** события, реактивность, pub/sub.

```python
class Subject:
    def __init__(self): self.subs = []
    def sub(self, f): self.subs.append(f)
    def notify(self, v):
        for f in self.subs: f(v)

s = Subject()
s.sub(lambda v: print("got", v))
s.notify(42)
```

---

### State (Состояние)
**Идея:** поведение объекта зависит от текущего состояния.  
**Когда:** автоматы, жизненные циклы, UI‑режимы.

```python
class State:
    def on(self, ctx): ...
    def off(self, ctx): ...

class On(State):
    def off(self, ctx): print("turn off"); ctx.state = Off()

class Off(State):
    def on(self, ctx): print("turn on"); ctx.state = On()

class Switch:
    def __init__(self): self.state = Off()
    def on(self): self.state.on(self)
    def off(self): self.state.off(self)
```

---

### Strategy (Стратегия)
**Идея:** взаимозаменяемые алгоритмы под одним интерфейсом.  
**Когда:** сортировки, маршрутизация, ценообразование.

```python
def add(a,b): return a+b
def mul(a,b): return a*b

class Ctx:
    def __init__(self, strat): self.strat = strat
    def exec(self, a,b): return self.strat(a,b)

ctx = Ctx(add); ctx.exec(2,3); ctx.strat = mul; ctx.exec(2,3)
```

---

### Template Method (Шаблонный метод)
**Идея:** скелет алгоритма в базовом классе; шаги — в подклассах.  
**Когда:** одинаковый пайплайн с вариациями шагов.

```python
class ETL:
    def run(self):
        data = self.extract()
        data = self.transform(data)
        self.load(data)
    def extract(self): ...
    def transform(self, d): return d
    def load(self, d): ...

class CSV_ETL(ETL):
    def extract(self): return ["1","2"]
    def load(self, d): print("loaded", d)
```

---

### Visitor (Посетитель)
**Идея:** вынос операций над объектной структурой в отдельный объект‑посетитель.  
**Когда:** нужно добавлять новые операции без изменения узлов.

```python
class Number: 
    def __init__(self, v): self.v = v
    def accept(self, v): v.visit_number(self)

class Printer:
    def visit_number(self, n): print(n.v)

ast = [Number(1), Number(2)]
p = Printer()
for node in ast: node.accept(p)
```

---

## Памятка по выбору паттерна

- **Сложное создание?** → Builder / Abstract Factory / Factory Method / Prototype  
- **Связи и граф объектов?** → Composite / Bridge / Facade / Adapter  
- **Добавить поведение без наследования?** → Decorator / Proxy  
- **Много однотипных объектов?** → Flyweight  
- **Взаимодействия/алгоритмы?** → Strategy / Template Method / Visitor / Interpreter  
- **События и координация?** → Observer / Mediator / Chain of Responsibility  
- **Жизненный цикл/режимы?** → State  
- **История/откаты?** → Memento

## Python‑советы

- Используйте **модули** как Singleton.  
- Вместо сложного Iterator чаще подходят **генераторы** и `itertools`.  
- Strategy удобно выражается **функциями**/словарями диспетчеризации.  
- Decorator — это и паттерн, и **@синтаксис** в Python.  
- Dataclasses помогают Builder/Composite/State сделать чище.  
- Для Proxy/Decorator полезны `functools.wraps`, для flyweight — пулы/кеши.  

---

© GoF каталог (23) адаптирован под Python 3. Паттерны — не самоцель: применяйте, когда они упрощают код и архитектуру.
