import tkinter as tk
from ui.app import CodeMateUI


def main():
    root = tk.Tk()
    CodeMateUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
