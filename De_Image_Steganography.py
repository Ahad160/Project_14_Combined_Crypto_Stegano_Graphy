from stegano import lsb


# Function to extract text from an image
def extract_text_from_image(image_path):
    secret = lsb.reveal(image_path)
    return secret


output_image = r"E:\Codeing\Python Language\Projects\Project_14_DARK_Crypto_Stegano_Graphy\Image.png"

# hide_text_in_image(input_image, output_image, secret_message)
extracted_message = extract_text_from_image(output_image)

# print("Original message:", secret_message)
print("Extracted message:", extracted_message)
