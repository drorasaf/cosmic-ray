import ast


class PrintVisitor(ast.NodeVisitor):
    def __init__(self):
        self.indent = ''

    def generic_visit(self, node):
        print(self.indent, repr(node))
        self.indent += '    '
        super().generic_visit(node)  # pylint:disable=missing-super-argument
        self.indent = self.indent[:-4]

    def visit_Num(self, node):  # noqa
        print('a number:', node)


def dump_mod():
    import mod
    with open(mod.__file__, 'rt') as module_file:
        nodes = ast.parse(module_file.read())
    PrintVisitor().visit(nodes)
