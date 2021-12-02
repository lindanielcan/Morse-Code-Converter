import tkinter

morse_code_icon = "./images/morse-code.png"

class UserInterface():
    def __init__(self):
        """This class will be using tkinter library to create a Gui."""
        self.window = tkinter.Tk()
        self.window.title('Morse Code Converter')
        self.my_canva = tkinter.Canvas(height=500, width=500, bg='white')
        self.my_canva.config()
        self.my_canva.pack(padx=20, pady=20)

    def loop(self):
        self.window.mainloop()
