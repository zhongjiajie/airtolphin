from airtolphin.core.rule import Rule


class MyRule3(Rule):
    spec = "operator"

    def __init__(self):
        print("MyPlugin3 instance created")

    def do_work(self):
        print("Do nothing.")
