import ast


class ASTAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.findings = []

    def visit_FunctionDef(self, node):
        if len(node.body) > 50:
            self.findings.append(
                f"Function '{node.name}' is too long ({len(node.body)} lines)."
            )
        self.generic_visit(node)

    def visit_While(self, node):
        self.findings.append(
            "While loop detected. Ensure proper exit condition."
        )
        self.generic_visit(node)

    def visit_Try(self, node):
        for handler in node.handlers:
            if handler.type is None:
                self.findings.append(
                    "Bare except detected. Catch specific exceptions."
                )
        self.generic_visit(node)


def run_ast_checks(code: str):
    try:
        tree = ast.parse(code)
        analyzer = ASTAnalyzer()
        analyzer.visit(tree)
        return analyzer.findings or ["No AST-level issues found."]
    except SyntaxError as e:
        return [f"SyntaxError at line {e.lineno}: {e.msg}"]
