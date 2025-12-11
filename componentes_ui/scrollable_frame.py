import tkinter as tk
from tkinter import ttk

class ScrollableFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Canvas + Scrollbar
        canvas = tk.Canvas(self, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)

        # CAMBIO IMPORTANTE → usar tk.Frame (ya no ttk.Frame)
        self.scrollable_frame = tk.Frame(canvas, bg="#f4f6f9")

        # Ajustar scrollregion al tamaño interno
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.canvas = canvas

        # scroll con rueda del mouse
        self.scrollable_frame.bind("<Enter>", self._bind_mousewheel)
        self.scrollable_frame.bind("<Leave>", self._unbind_mousewheel)

    def _bind_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")
