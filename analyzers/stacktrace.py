def analyze_stacktrace(traceback_text: str):
    issues = []

    if "NameError" in traceback_text:
        issues.append("NameError: variable or function not defined.")

    if "TypeError" in traceback_text:
        issues.append("TypeError: incorrect type used in operation or function call.")

    if "IndexError" in traceback_text:
        issues.append("IndexError: list or tuple index out of range.")

    if "KeyError" in traceback_text:
        issues.append("KeyError: dictionary key not found.")

    if "AttributeError" in traceback_text:
        issues.append("AttributeError: object has no such attribute.")

    if not issues:
        issues.append("Unclassified error. Check last line of traceback.")

    return issues
