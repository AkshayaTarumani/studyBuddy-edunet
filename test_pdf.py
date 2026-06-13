from pdfutils import extract_text_from_pdf

# open a PDF file in your system
with open(r"c:\Users\Akshya\Downloads\UNIT 3 DM.pptx", "rb") as f:
    text = extract_text_from_pdf(f)

print(text)