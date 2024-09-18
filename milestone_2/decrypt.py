def simple_decrypt(encrypted_text): #a text decryption function that converts ASCII codes back to characters.
    decrypted_text = ""
    ascii_values = encrypted_text.split()  #Separate by spaces
    for value in ascii_values:
        decrypted_text += chr(int(value))  #Convert the ASCII-code back to a character
    return decrypted_text

if __name__ == "__main__":
    encrypted_text = "72 101 108 108 111"  # ASCII-code to "Hello"
    decrypted = simple_decrypt(encrypted_text)
    print("Decrypted text:", decrypted)