def read_multiline_input(prompt: str = "") -> str:
    if prompt:
        print(prompt)

    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break

        if not line.strip():
            break

        lines.append(line)

    return "\n".join(lines)


def print_header(title: str):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def print_list(items):
    for item in items:
        print(f"- {item}")
