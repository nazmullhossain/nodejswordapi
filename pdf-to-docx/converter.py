import sys
import os
from pdf2docx import parse

def convert_pdf_to_docx(pdf_path, docx_path):
    try:
        # Convert to absolute paths
        pdf_path = os.path.abspath(pdf_path)
        docx_path = os.path.abspath(docx_path)
        
        print(f"Absolute PDF path: {pdf_path}")
        print(f"Absolute DOCX path: {docx_path}")
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(docx_path), exist_ok=True)
        
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