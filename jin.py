from tkinter import *

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Test")
        self.root.geometry("500x350")
        self.root.resizable(False, False)
        #more

        Label(self.root,text="SEND OFFLINE SMS", font="Dungeon 20").pack(side=TOP,pady=10) #Unchangable

        Label(self.root,text="Phone No: ", font="Bell 15").place(x=25,y=55) #Unchangable

        #Phone Number
        self.phone = Entry(self.root, font="consolas 15",bd=3,)
        self.phone.pack()

        #sms details
        self.detail = Label(self.root,font="consolas 15")
        self.detail.pack(fill=BOTH)

        #main sms
        self.msg = Text(self.root,font="consolas 15",height=5)
        self.msg.pack(fill=BOTH)

        #send button
        self.send = Button(self.root,text="Send",font="Prime 20",bg="lightgrey",command=self.send)
        self.send.pack(fill=BOTH,side=BOTTOM)

    def send(self):
        import random # Just For testing :) 
        self.detail.config(text=f"SMS sended {random.randint(1,100)}")
        
if __name__ == "__main__":
    win = Tk()
    obj = Main(win)
    win.mainloop()

