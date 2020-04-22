from tkinter import *
from tkinter.ttk import *

# https://blog.tecladocode.com/tkinter-scrollable-frames/
# Start of scrollable frame
class scrollableFrame(Frame):
    def __init__(self, window, W, H, X, Y):
        container = Frame(window, width=W, height=H)
        self.canvas = Canvas(container, width=W, height=H)
        scrollbar = Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas, width=W, height=H)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        container.place(x=X, y=Y)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        # End of scrollable frame