import os

# Function to encrypt the text using Caesar Cipher
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Shift the letter and handle wrapping around alphabet
            start = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr(start + (ord(char) - start + shift) % 26)
        else:
            encrypted_text += char
    return encrypted_text

# Function to decrypt the text using Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)  # Decrypting is just reversing the shift

# Function to process file encryption
def encrypt_file(file_path, shift):
    if not os.path.exists(file_path):
        print("Error: File does not exist.")
        return

    with open(file_path, 'r') as file:
        content = file.read()

    encrypted_content = encrypt(content, shift)

    encrypted_file_path = f"encrypted_{os.path.basename(file_path)}"
    with open(encrypted_file_path, 'w') as encrypted_file:
        encrypted_file.write(encrypted_content)

    print(f"File encrypted successfully: {encrypted_file_path}")

# Function to process file decryption
def decrypt_file(file_path, shift):
    if not os.path.exists(file_path):
        print("Error: File does not exist.")
        return

    with open(file_path, 'r') as file:
        encrypted_content = file.read()

    decrypted_content = decrypt(encrypted_content, shift)

    decrypted_file_path = f"decrypted_{os.path.basename(file_path)}"
    with open(decrypted_file_path, 'w') as decrypted_file:
        decrypted_file.write(decrypted_content)

    print(f"File decrypted successfully: {decrypted_file_path}")

# Main function to interact with user
def main():
    while True:
        print("\nFile Encryption/Decryption Menu:")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            file_path = input("Enter the file path to encrypt: ")
            shift = int(input("Enter shift value for encryption: "))
            encrypt_file(file_path, shift)
        elif choice == "2":
            file_path = input("Enter the file path to decrypt: ")
            shift = int(input("Enter shift value for decryption: "))
            decrypt_file(file_path, shift)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
