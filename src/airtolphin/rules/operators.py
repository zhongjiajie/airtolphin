import libcst as cst


class Operators:
    attr_keep_old = (
        "whitespace_before_args",
    )

    def __init__(self, node: cst.Assign) -> None:
        self.node = node

    def run(self) -> cst.Assign:
        # keep all cst.Call attribute which have to change
        call_kwargs = {}
        call_args = []
        call = cst.ensure_type(self.node.value, cst.Call)
        # covert `airflow.operators.bash.BashOperator` assign
        if cst.ensure_type(call.func, cst.Name).value == "BashOperator":
            call_kwargs["func"] = cst.Name("Shell")
            for arg in call.args:
                arg_keyword = cst.ensure_type(arg.keyword, cst.Name).value
                if arg_keyword == "task_id":
                    call_args.append(arg.with_changes(keyword=cst.Name("name")))
                elif arg_keyword == "bash_command":
                    call_args.append(arg.with_changes(keyword=cst.Name("command")))
            call_kwargs["args"] = call_args
            for attr in self.attr_keep_old:
                call_kwargs[attr] = getattr(call, attr)
            return self.node.with_changes(value=cst.Call(**call_kwargs))
        return self.node