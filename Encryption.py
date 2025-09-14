# use this 'source Encryption/bin/activate'

# this is something like chat system 

from cryptography.fernet import Fernet

while True:
    try:
        # 1. Input message
        message = input("The message you want to send: ")

        # 2. Generate key
        key = Fernet.generate_key()
        print("Key:", key)

        # 3. Create Fernet cipher object
        cipher = Fernet(key)

        # 4. Convert message to bytes
        message_bytes = message.encode()

        # 5. Encrypt the message
        encrypted_message = cipher.encrypt(message_bytes)
        print("Encrypted message:", encrypted_message)

        # 6. Decrypt the message
        decrypted_bytes = cipher.decrypt(encrypted_message)
        original_message = decrypted_bytes.decode()
        print("Decrypted message:", original_message)

        # 6. Decrypt the message
        decrypted_bytes = cipher.decrypt(encrypted_message)
        original_message = decrypted_bytes.decode()
        print("Decrypted message:", original_message)
    
    except Exception as e:
        print(e)

    finally:
        quit = input("you want to continue (y/n): ").lower()
        if quit == 'n':
            print("thanks for using our app")
            break

