from airtolphin.core.rule import Rule


class MyRule2(Rule):
    spec = "operator"

    def __init__(self):
        print("MyPlugin2 instance created")

    def do_work(self):
        print("Do something else")
