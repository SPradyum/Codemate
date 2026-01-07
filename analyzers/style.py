def check_style(code: str):
    warnings = []

    lines = code.splitlines()

    for i, line in enumerate(lines, start=1):
        if len(line) > 100:
            warnings.append(f"Line {i} exceeds 100 characters.")

        if "\t" in line:
            warnings.append(f"Line {i} contains a tab character.")

        if line.rstrip() != line:
            warnings.append(f"Line {i} has trailing whitespace.")

    if not warnings:
        warnings.append("No basic style issues detected.")

    return warnings
