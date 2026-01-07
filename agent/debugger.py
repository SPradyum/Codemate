def explain_traceback(traceback_text: str) -> str:
    explanations = []

    if not traceback_text.strip():
        return "No traceback provided."

    if "NameError" in traceback_text:
        explanations.append(
            "NameError detected:\n"
            "- A variable or function is used before being defined.\n"
            "- Check spelling and scope."
        )

    if "TypeError" in traceback_text:
        explanations.append(
            "TypeError detected:\n"
            "- Operation or function used with incompatible data types.\n"
            "- Verify function arguments and return values."
        )

    if "IndexError" in traceback_text:
        explanations.append(
            "IndexError detected:\n"
            "- Sequence index is out of range.\n"
            "- Check loop bounds or list length."
        )

    if "KeyError" in traceback_text:
        explanations.append(
            "KeyError detected:\n"
            "- Dictionary key does not exist.\n"
            "- Use dict.get() or check key existence."
        )

    if "AttributeError" in traceback_text:
        explanations.append(
            "AttributeError detected:\n"
            "- Object does not have the accessed attribute.\n"
            "- Verify object type."
        )

    if "ImportError" in traceback_text or "ModuleNotFoundError" in traceback_text:
        explanations.append(
            "Import error detected:\n"
            "- Module not found or incorrect import path.\n"
            "- Check virtual environment and PYTHONPATH."
        )

    if not explanations:
        explanations.append(
            "General Python Error:\n"
            "- Check the last line of the traceback for the error type.\n"
            "- Focus on the file name and line number mentioned."
        )

    return "\n\n".join(explanations)
