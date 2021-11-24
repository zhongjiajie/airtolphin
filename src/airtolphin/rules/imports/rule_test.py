from airtolphin.core.rule import Rule


class MyRule1(Rule):
    spec = "import"

    def __init__(self):
        print("MyPlugin1 instance created")

    def do_work(self):
        print("Do something")
