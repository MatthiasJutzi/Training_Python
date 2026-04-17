# Ceasar Cipher lab ctrl+k ctrl+c for comment ctrl+k ctrl+u for uncomment
# shift = 5
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# shifted_alphabet = alphabet[shift:] + alphabet[:shift]
# translation_table = str.maketrans(alphabet, shifted_alphabet)
# text = "hello world"
# encrypted_text = text.translate(translation_table)
# print(encrypted_text)

def caesar():
    shift = 5
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet, shifted_alphabet)
    text = "hello world"
    encrypted_text = text.translate(translation_table)
    print(encrypted_text)

caesar()