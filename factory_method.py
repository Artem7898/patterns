# Создает объекты через фабрику.


class Button:
    def render(self): pass

class WindowsButton(Button):
    def render(self): print("Windows Button")

class LinuxButton(Button):
    def render(self): print("Linux Button")


class Dialog:
    def create_button(self) -> Button: pass

class WindowsDialog(Dialog):
    def create_button(self): return WindowsButton()

class LinuxDialog(Dialog):
    def create_button(self): return LinuxButton()


dialog = WindowsDialog()
button = dialog.create_button()
button.render()  # Windows Button
