def simple_encrypt(text):
    encrypted_text = ""
    for char in text:
        encrypted_text += str(ord(char)) + " "  # change symbol for ASCII-code
    return encrypted_text.strip()  #Remove the space at the end

if __name__ == "__main__":
    original_text = "Hello"
    encrypted = simple_encrypt(original_text)
    print("Encrypted text:", encrypted)