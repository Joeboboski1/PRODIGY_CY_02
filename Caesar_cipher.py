def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    # Adjust shift for decryption
    if mode == "decrypt":
        shift = -shift

    # Loop through each character in the text
    for char in text:
        # Check if character is a letter
        if char.isalpha():
            # Shift the character and maintain case
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            # If not a letter, add character without shifting
            result += char

    return result


# Get input from user
message = input("Enter your message: ")
shift_value = int(input("Enter shift value (positive for encryption, negative for decryption): "))
mode = input("Choose mode: 'encrypt' or 'decrypt': ").strip().lower()

# Perform encryption or decryption
if mode in ["encrypt", "decrypt"]:
    result = caesar_cipher(message, shift_value, mode)
    print(f"The {mode}ed message is: {result}")
else:
    print("Invalid mode selected. Choose 'encrypt' or 'decrypt'.")