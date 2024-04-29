
# Function to hide text within an image
def hide_text_in_image(input_image_path, output_image_path, secret_text):
    from stegano import lsb

    with open(secret_text,'r') as file:
        file=file.read()
        
    secret = lsb.hide(input_image_path, file)
    secret.save(output_image_path)

    print("Message hidden securely.")

    return output_image_path
