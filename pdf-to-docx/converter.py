import sys
from pdf2docx import parse

def convert_pdf_to_docx(pdf_path, docx_path):
    try:
        # This uses different internal methods that might work with newer PyMuPDF
        parse(pdf_path, docx_path)
        print("Conversion completed successfully")
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python converter.py <input_pdf> <output_docx>")
        sys.exit(1)
        
    pdf_path = sys.argv[1]
    docx_path = sys.argv[2]
    convert_pdf_to_docx(pdf_path, docx_path)