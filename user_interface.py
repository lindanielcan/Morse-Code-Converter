import tkinter
from morse_code_converter import MorseCodeConverter

morse_code_icon = "./images/morse-code.png"


class UserInterface():
    def __init__(self):
        """
        This class will be using tkinter library to create a Gui.
        Objects such as buttons, text boxes, labels are initiated in the constructor.
        """
        self.window = tkinter.Tk()
        self.code_converter = MorseCodeConverter()

        self.window.title('Morse Code Converter')
        self.window.config(bg='#96C7C1')
        self.my_canva = tkinter.Canvas(height=300, width=500, bg='#F0E9D2', highlightthickness=0)

        self.user_message_label = self.my_canva.create_text(85, 50, fill="black", font="Arial",
                                                            text="Your message: ")
        self.morse_code_label = self.my_canva.create_text(92, 80, fill="black", font="Arial",
                                                          text="Morse Code: ")
        self.result_label = self.my_canva.create_text(113, 112, fill="black", font="Arial",
                                                      text="Result: ")

        self.user_message = tkinter.Entry(self.window, width=50)
        self.user_message_window = self.my_canva.create_window(300, 50, window=self.user_message)
        self.morse_code = tkinter.Entry(self.window, width=50)
        self.morse_code_window = self.my_canva.create_window(300, 80, window=self.morse_code)
        self.result = tkinter.Text(self.window, width=42, height=10)
        self.result_window = self.my_canva.create_window(297, 170, window=self.result)

        self.copy_result_button = tkinter.Button(self.window, width=15, height=1, bg='#E6DDC4',
                                                 activebackground='#F0E9D2', text='Copy result',
                                                 font=('Ariel', 10, 'bold'), command=self.copy_result)
        self.copy_result_button_window = self.my_canva.create_window(212, 260, window=self.copy_result_button)

        self.clear_button = tkinter.Button(self.window, width=15, height=1, bg='#E6DDC4',
                                           activebackground='#F0E9D2', text='Clear',
                                           font=('Ariel', 10, 'bold'), command=self.clear)
        self.clear_result_button_window = self.my_canva.create_window(360, 260, window=self.clear_button)

        self.my_canva.grid(padx=20, pady=20, column=0, row=0, columnspan=2)

        self.encode_button = tkinter.Button(width=10, height=3, bg='#89B5AF',
                                            text='Encode', font=('Ariel', 15, 'bold'),
                                            activebackground='#96C7C1', command=self.show_encoded_result)
        self.encode_button.grid(column=0, row=1, padx=20, pady=30)

        self.decode_button = tkinter.Button(width=10, height=3, bg='#89B5AF',
                                            text='Decode', font=('Ariel', 15, 'bold'),
                                            activebackground='#96C7C1', command=self.show_decoded_result)
        self.decode_button.grid(column=1, row=1, padx=20, pady=30)

    def get_message_entry_box_text(self):
        """
        :return: string from the message entry.
        """
        return self.user_message.get()

    def get_morse_code_entry_text(self):
        """
        :return: string from morse code entry text box.
        """
        return self.morse_code.get()

    def show_encoded_result(self):
        """
        Shows the encoded morse code in the result text box.
        """
        self.result.delete(1.0, 'end-1c')
        self.result.insert(1.0, self.code_converter.encode(self.get_message_entry_box_text()))

    def show_decoded_result(self):
        """
        Shows the decoded message in the result text box.
        """
        self.result.delete(1.0, 'end-1c')
        self.result.insert(1.0, self.code_converter.decode(self.get_morse_code_entry_text()))

    def copy_result(self):
        """
        Copies the result in the result text box.
        """
        self.window.clipboard_clear()
        self.window.clipboard_append(self.result.get(1.0, 'end-1c'))

    def clear(self):
        """
        Clears the message entry box, morse code entry box, and result text box.
        """
        self.user_message.delete(0, 'end')
        self.morse_code.delete(0, 'end')
        self.result.delete(1.0, 'end-1c')

    def loop(self):
        self.window.mainloop()
