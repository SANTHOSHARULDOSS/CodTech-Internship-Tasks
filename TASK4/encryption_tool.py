from cryptography.fernet import Fernet
import os

def generate_key():
    """Generates a key and saves it into a file"""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to 'secret.key'")

def load_key():
    """Loads the key from the current directory named `secret.key`"""
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    """Encrypts the file"""
    key = load_key()
    f = Fernet(key)
    
    with open(filename, "rb") as file:
        file_data = file.read()
        
    encrypted_data = f.encrypt(file_data)
    
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    print(f"File '{filename}' has been ENCRYPTED successfully!")

def decrypt_file(filename):
    """Decrypts the file"""
    key = load_key()
    f = Fernet(key)
    
    with open(filename, "rb") as file:
        encrypted_data = file.read()
        
    decrypted_data = f.decrypt(encrypted_data)
    
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print(f"File '{filename}' has been DECRYPTED successfully!")

# --- MAIN MENU ---
if __name__ == "__main__":
    import os
    
    print("--- ADVANCED ENCRYPTION TOOL ---")
    
    # Check if key exists, if not, make one
    if not os.path.exists("secret.key"):
        generate_key()
    else:
        print("Key file found.")

    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    target_file = "secret_data.txt" # You can change this to input() if you want

    try:
        if choice == 'E':
            encrypt_file(target_file)
        elif choice == 'D':
            decrypt_file(target_file)
        else:
            print("Invalid choice.")
    except Exception as e:
        print(f"Error: {e}")
