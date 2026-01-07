from agent.debugger import explain_traceback
from agent.refactor import analyze_code, suggest_refactor
from agent.tests import generate_tests


def run_agent():
    print("=" * 60)
    print("CodeMate – Python Coding & Debugging Agent")
    print("=" * 60)

    while True:
        print("\nChoose an option:")
        print("1. Explain Python traceback")
        print("2. Analyze Python code")
        print("3. Suggest refactors")
        print("4. Generate unit tests")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            print("\nPaste traceback (end with empty line):")
            tb = _read_multiline()
            print("\nExplanation:\n")
            print(explain_traceback(tb))

        elif choice == "2":
            print("\nPaste Python code (end with empty line):")
            code = _read_multiline()
            issues = analyze_code(code)
            print("\nAnalysis:")
            for issue in issues:
                print(" -", issue)

        elif choice == "3":
            print("\nPaste Python code (end with empty line):")
            code = _read_multiline()
            print("\nRefactor Suggestions:\n")
            print(suggest_refactor(code))

        elif choice == "4":
            print("\nPaste Python code (end with empty line):")
            code = _read_multiline()
            print("\nGenerated Tests:\n")
            print(generate_tests(code))

        elif choice == "5":
            print("Exiting CodeMate.")
            break

        else:
            print("Invalid choice. Try again.")


def _read_multiline():
    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)
    return "\n".join(lines)
