import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Example usage
pdf_path = 'C://Users//KINJAL KANJILAL//Desktop//KNOWYOURPDF//HIT Placement Policy (Jul 2021).pdf'  # Replace with the path to your PDF file
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)