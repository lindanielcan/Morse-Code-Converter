from morse_code_converter import MorseCodeConverter
from user_interface import UserInterface

code_converter = MorseCodeConverter()
UI = UserInterface()

# message = input(
#     "Hi, do you need to encode your text or do you need to decode your morse code. Type 'encode' for encode or "
#     "'decode' for decode.")
#
# if message == 'encode':
#     text = input("Hi, please enter the text you need to convert into morse code.\n")
#     print(f"Here's the morse code for your input: {code_converter.encode(text)}")
# elif message == 'decode':
#     text = input("Hi, please enter the morse code that you want to be decoded.\n")
#     print(f"Here's the text decoded from your input: {code_converter.decode(text)}")

UI.loop()