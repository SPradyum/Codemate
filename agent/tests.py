import ast
import textwrap


def generate_tests(code: str) -> str:
    try:
        tree = ast.parse(code)
        functions = [
            node.name for node in tree.body
            if isinstance(node, ast.FunctionDef)
        ]

        if not functions:
            return "No functions found to generate tests."

        lines = [
            "import unittest",
            "",
            "class TestGeneratedFunctions(unittest.TestCase):",
        ]

        for fn in functions:
            lines.append(
                textwrap.indent(
                    f"""def test_{fn}(self):
    # TODO: provide meaningful input values
    try:
        result = {fn}()
    except Exception as e:
        self.fail(f"{fn} raised an exception: {{e}}")
    self.assertIsNotNone(result)
""",
                    "    ",
                )
            )

        lines.extend([
            "",
            "if __name__ == '__main__':",
            "    unittest.main()"
        ])

        return "\n".join(lines)

    except SyntaxError as e:
        return f"SyntaxError at line {e.lineno}: {e.msg}"
    except Exception as e:
        return f"Failed to generate tests: {e}"
