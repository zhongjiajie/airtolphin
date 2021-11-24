from abc import abstractmethod, ABC
from typing import Dict, List


class Rule(ABC):
    """Base class for all plugins. Singleton instances of subclasses are created
    automatically and stored in Plugin.plugins class field."""
    spec = None
    plugins: Dict[str, List] = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.spec is None:
            raise ValueError("Attribute `spec` must be provider.")
        if cls.spec in cls.plugins:
            addition = cls.plugins[cls.spec]
            addition.append(cls())
            cls.plugins[cls.spec] = addition
        else:
            cls.plugins[cls.spec] = [cls()]

    @abstractmethod
    def do_work(self):
        raise NotImplementedError("Subclass must implement function do_work.")

    @classmethod
    def run_all_work(cls, spec="all"):
        if spec == "all":
            for plugin_list in cls.plugins.values():
                for plugin in plugin_list:
                    plugin.do_work()
        elif spec not in cls.plugins:
            raise ValueError("Spec `%s` not in exists plugins list", spec)
        else:
            for plugin in cls.plugins[spec]:
                plugin.do_work()


class MyRule1(Rule):
    spec = "import"

    def __init__(self):
        print("MyPlugin1 instance created")

    def do_work(self):
        print("Do something")


class MyRule2(Rule):
    spec = "operator"

    def __init__(self):
        print("MyPlugin2 instance created")

    def do_work(self):
        print("Do something else")


Rule.run_all_work()

# for plugin in Plugin.plugins:
#     plugin.do_work()
