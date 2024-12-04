import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'  # Update this if Homebrew installed it elsewhere

# Use the OCR function as before
printed_text = extract_text_with_tesseract(aligned_img, x_cm, y_cm, w_cm, h_cm)
print("Extracted Text from Printed Text Box:")
print(printed_text)
