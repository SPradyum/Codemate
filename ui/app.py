import tkinter as tk
from tkinter import ttk, scrolledtext

from agent.debugger import explain_traceback
from agent.refactor import analyze_code, suggest_refactor
from agent.tests import generate_tests


class CodeMateUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CodeMate – Python Coding Assistant")
        self.root.geometry("1100x700")
        self.root.minsize(1000, 650)
        self.root.configure(bg="#0b1220")

        self._apply_theme()
        self._build_ui()

    # ---------------- THEME ----------------
    def _apply_theme(self):
        style = ttk.Style()
        style.theme_use("default")

        style.configure(
            "TButton",
            font=("Segoe UI", 10),
            padding=8
        )

        style.configure(
            "Toolbar.TFrame",
            background="#020617"
        )

        style.configure(
            "Body.TFrame",
            background="#0b1220"
        )

    # ---------------- UI ----------------
    def _build_ui(self):
        # ---------- TOP BAR ----------
        top = ttk.Frame(self.root, style="Toolbar.TFrame", height=60)
        top.pack(fill="x")

        tk.Label(
            top,
            text="CodeMate",
            fg="#38bdf8",
            bg="#020617",
            font=("Segoe UI", 20, "bold")
        ).pack(side="left", padx=20)

        tk.Label(
            top,
            text="Python Debugging & Coding Assistant",
            fg="#94a3b8",
            bg="#020617",
            font=("Segoe UI", 11)
        ).pack(side="left")

        # ---------- MAIN BODY ----------
        body = ttk.Frame(self.root, style="Body.TFrame")
        body.pack(fill="both", expand=True, padx=12, pady=12)

        body.columnconfigure(0, weight=1)
        body.columnconfigure(1, weight=1)
        body.rowconfigure(1, weight=1)

        # ---------- INPUT ----------
        tk.Label(
            body,
            text="Input (Code / Traceback)",
            fg="#e5e7eb",
            bg="#0b1220",
            font=("Segoe UI", 12, "bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 6))

        self.input_box = scrolledtext.ScrolledText(
            body,
            wrap="word",
            font=("Consolas", 11),
            bg="#020617",
            fg="#e5e7eb",
            insertbackground="white",
            relief="flat"
        )
        self.input_box.grid(row=1, column=0, sticky="nsew", padx=(0, 10))

        # ---------- OUTPUT ----------
        tk.Label(
            body,
            text="Output",
            fg="#e5e7eb",
            bg="#0b1220",
            font=("Segoe UI", 12, "bold")
        ).grid(row=0, column=1, sticky="w", pady=(0, 6))

        self.output_box = scrolledtext.ScrolledText(
            body,
            wrap="word",
            font=("Consolas", 11),
            bg="#020617",
            fg="#22c55e",
            insertbackground="white",
            relief="flat",
            state="disabled"
        )
        self.output_box.grid(row=1, column=1, sticky="nsew")

        # ---------- ACTION BAR ----------
        actions = ttk.Frame(self.root)
        actions.pack(fill="x", padx=12, pady=(0, 12))

        ttk.Button(actions, text="Explain Error", command=self._explain).pack(
            side="left", padx=6
        )
        ttk.Button(actions, text="Analyze Code", command=self._analyze).pack(
            side="left", padx=6
        )
        ttk.Button(actions, text="Refactor", command=self._refactor).pack(
            side="left", padx=6
        )
        ttk.Button(actions, text="Generate Tests", command=self._tests).pack(
            side="left", padx=6
        )

        ttk.Button(actions, text="Clear", command=self._clear).pack(
            side="right", padx=6
        )

    # ---------------- HELPERS ----------------
    def _get_input(self):
        return self.input_box.get("1.0", tk.END).strip()

    def _set_output(self, text):
        self.output_box.configure(state="normal")
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, text)
        self.output_box.configure(state="disabled")

    def _clear(self):
        self.input_box.delete("1.0", tk.END)
        self._set_output("")

    # ---------------- ACTIONS ----------------
    def _explain(self):
        text = self._get_input()
        if not text:
            self._set_output("No traceback provided.")
            return
        self._set_output(explain_traceback(text))

    def _analyze(self):
        code = self._get_input()
        issues = analyze_code(code)
        self._set_output("\n".join(f"- {i}" for i in issues))

    def _refactor(self):
        code = self._get_input()
        self._set_output(suggest_refactor(code))

    def _tests(self):
        code = self._get_input()
        self._set_output(generate_tests(code))
