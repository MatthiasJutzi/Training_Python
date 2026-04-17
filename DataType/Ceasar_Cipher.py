# Ceasar Cipher lab ctrl+k ctrl+c for comment ctrl+k ctrl+u for uncomment
# shift = 5
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# shifted_alphabet = alphabet[shift:] + alphabet[:shift]
# translation_table = str.maketrans(alphabet, shifted_alphabet)
# text = "hello world"
# encrypted_text = text.translate(translation_table)
# print(encrypted_text)

def caesar(text, shift):

    if isinstance(shift, int):
        return "Shift must be an integer value."
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)
   
encrypted_text = caesar("freeCodeCamp", 3)
print(encrypted_text)
