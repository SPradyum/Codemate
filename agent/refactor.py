import ast


class CodeInspector(ast.NodeVisitor):
    def __init__(self):
        self.issues = []

    def visit_FunctionDef(self, node):
        if len(node.body) > 40:
            self.issues.append(
                f"Function '{node.name}' is long ({len(node.body)} lines). "
                "Consider breaking it into smaller functions."
            )
        self.generic_visit(node)

    def visit_Try(self, node):
        for handler in node.handlers:
            if handler.type is None:
                self.issues.append(
                    "Bare except detected. Catch specific exceptions instead."
                )
        self.generic_visit(node)

    def visit_Import(self, node):
        for alias in node.names:
            if alias.asname:
                self.issues.append(
                    f"Aliased import '{alias.name} as {alias.asname}'. "
                    "Ensure clarity."
                )
        self.generic_visit(node)


def analyze_code(code: str):
    try:
        tree = ast.parse(code)
        inspector = CodeInspector()
        inspector.visit(tree)
        return inspector.issues or ["No major structural issues found."]
    except SyntaxError as e:
        return [f"SyntaxError at line {e.lineno}: {e.msg}"]


def suggest_refactor(code: str) -> str:
    suggestions = []

    if "== None" in code:
        suggestions.append("Use `is None` instead of `== None`.")

    if "print(" in code:
        suggestions.append("Consider using the `logging` module instead of print().")

    if "except:" in code:
        suggestions.append("Avoid bare except. Catch specific exceptions.")

    if not suggestions:
        suggestions.append("Code looks clean. Only minor refactoring may be needed.")

    return "\n".join(f"- {s}" for s in suggestions)
