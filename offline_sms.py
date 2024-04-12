from tkinter import *

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Test")
        self.root.geometry("500x350")
        self.root.resizable(False, False)
        #more

        Label(self.root, text="SEND OFFLINE SMS", font="Dungeon 20").pack(side=TOP, pady=10) #Unchangeable

        Label(self.root, text="Phone No: ", font="Bell 15").place(x=25, y=55) #Unchangeable

        # Phone Number
        self.phone = WatermarkEntry(self.root, font="consolas 15", bd=3, watermark="Enter phone number")
        self.phone.pack()

        # SMS details
        self.detail = Label(self.root, font="consolas 15")
        self.detail.pack(fill=BOTH, pady=29)

        # Main SMS
        self.msg = WatermarkText(self.root, font="consolas 15", height=5, watermark="Enter your message here")
        self.msg.pack(fill=BOTH)

        # Send button
        self.send = Button(self.root, text="Send", font="Prime 20", bg="lightgrey", command=self.send)
        self.send.pack(fill=BOTH, side=BOTTOM)

    def send(self):
        import random  # Just For testing :)
        self.detail.config(text=f"SMS sent {random.randint(1, 100)}")


class WatermarkText(Text):
    def __init__(self, master=None, watermark="", **kwargs):
        super().__init__(master, **kwargs)
        self.watermark = watermark
        self.default_fg_color = self.cget("fg")
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
        self.put_watermark()

    def put_watermark(self):
        self.insert("1.0", self.watermark)
        self.tag_configure("watermark", foreground="grey")
        self.tag_add("watermark", "1.0", "end")

    def on_focus_in(self, event):
        if self.get("1.0", "end-1c") == self.watermark:
            self.delete("1.0", "end")
            self.config(foreground=self.default_fg_color)

    def on_focus_out(self, event):
        if not self.get("1.0", "end-1c"):
            self.put_watermark()


class WatermarkEntry(Entry):
    def __init__(self, master=None, watermark="", **kwargs):
        super().__init__(master, **kwargs)
        self.watermark = watermark
        self.default_fg_color = self["fg"]
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
        self.put_watermark()

    def put_watermark(self):
        if not self.get():
            self.insert(0, self.watermark)
            self["fg"] = "grey"

    def on_focus_in(self, event):
        if self.get() == self.watermark:
            self.delete(0, END)
            self["fg"] = self.default_fg_color

    def on_focus_out(self, event):
        if not self.get():
            self.put_watermark()


if __name__ == "__main__":
    win = Tk()
    obj = Main(win)
    win.mainloop()
