from typing import Dict, List


class Rule:
    """
    Base class for all rule plugins.

    Singleton instances of subclasses are created automatically and stored in rule.rules class field.
    """
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
