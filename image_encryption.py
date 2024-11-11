from PIL import Image

def encrypt_image(input_path, output_path, key=50):
    # Open the image and convert it to RGB format
    img = Image.open(input_path)
    img = img.convert("RGB")
    pixels = img.load()

    # Encrypt the image by modifying pixel values
    for i in range(img.size[0]):  # Width
        for j in range(img.size[1]):  # Height
            r, g, b = pixels[i, j]
            # Example transformation: Add the key value to each color channel
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    # Save the encrypted image
    img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, key=50):
    # Open the encrypted image
    img = Image.open(input_path)
    img = img.convert("RGB")
    pixels = img.load()

    # Decrypt the image by reversing the pixel manipulation
    for i in range(img.size[0]):  # Width
        for j in range(img.size[1]):  # Height
            r, g, b = pixels[i, j]
            # Reverse transformation by subtracting the key
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    # Save the decrypted image
    img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

# Example usage
encrypt_image('/home/yanney/Downloads/78.jpg', '/home/yanney/Downloads/78.jpg', key=50)
decrypt_image('/home/yanney/Downloads/78.jpg', '/home/yanney/Downloads/78.jpg', key=50)
