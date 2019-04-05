from tkinter import *
from views.start_menu import Menu



if __name__ == "__main__":

    root = Tk()
    root.minsize(640, 640)
    Menu(root)
    root.mainloop()