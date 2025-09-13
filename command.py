# Инкапсулирует действие в объект.


class Command:
    def execute(self): pass

class LightOn(Command):
    def execute(self):
        print("Свет включен")

class RemoteControl:
    def __init__(self):
        self.commands = []

    def add(self, command):
        self.commands.append(command)

    def run(self):
        for cmd in self.commands:
            cmd.execute()

remote = RemoteControl()
remote.add(LightOn())
remote.run()
