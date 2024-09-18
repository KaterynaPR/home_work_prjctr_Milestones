def simple_encrypt(text): #a simple function for ‘encrypting’ text that simply changes each character to its ASCII code.
    encrypted_text = ""
    for char in text:
        encrypted_text += str(ord(char)) + " "  # change symbol for ASCII-code
    return encrypted_text.strip()  #Remove the space at the end

if __name__ == "__main__":
    original_text = "Hello"
    encrypted = simple_encrypt(original_text)
    print("Encrypted text:", encrypted)