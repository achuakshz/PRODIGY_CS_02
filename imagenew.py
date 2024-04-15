from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size
    
    # Convert the image to RGB mode
    img = img.convert("RGB")
    
    # Encrypt the image by applying a simple XOR operation with the key to each pixel
    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            r ^= key
            g ^= key
            b ^= key
            encrypted_pixels.append((r, g, b))
    
    # Create a new image with the encrypted pixels
    encrypted_img = Image.new("RGB", (width, height))
    encrypted_img.putdata(encrypted_pixels)
    
    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully!")

def decrypt_image(image_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    width, height = img.size
    
    # Convert the image to RGB mode
    img = img.convert("RGB")
    
    # Decrypt the image by applying the same XOR operation with the key to each pixel
    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            r ^= key
            g ^= key
            b ^= key
            decrypted_pixels.append((r, g, b))
    
    # Create a new image with the decrypted pixels
    decrypted_img = Image.new("RGB", (width, height))
    decrypted_img.putdata(decrypted_pixels)
    
    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully!")

# Example usage
image_path = "example_image.png"
key = 123  # You can use any integer key
encrypt_image(image_path, key)
decrypt_image("encrypted_image.png", key)