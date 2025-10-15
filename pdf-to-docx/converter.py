import sys
import os
import tempfile
from pdf2docx import parse

def convert_pdf_to_docx(pdf_path, docx_path):
    try:
        # Use absolute paths and ensure we're in a writable directory
        pdf_path = os.path.abspath(pdf_path)
        
        # Create the output in a temporary directory if the original path fails
        temp_dir = tempfile.gettempdir()
        temp_docx = os.path.join(temp_dir, os.path.basename(docx_path))
        
        print(f"Input PDF: {pdf_path}")
        print(f"Original output: {docx_path}")
        print(f"Temp output: {temp_docx}")
        
        # Convert PDF to DOCX
        parse(pdf_path, temp_docx)
        print("Conversion completed successfully")
        
        # Check if file was created in temp location
        if os.path.exists(temp_docx):
            print(f"File successfully created at: {temp_docx}")
            # If you need to move it to the original location, do it here
            # But on Railway, you might want to return the temp file path
            return temp_docx
        else:
            print("Error: File was not created in temp location")
            sys.exit(1)
            
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python converter.py <input_pdf> <output_docx>")
        sys.exit(1)
        
    pdf_path = sys.argv[1]
    docx_path = sys.argv[2]
    result_path = convert_pdf_to_docx(pdf_path, docx_path)
    print(f"Final file location: {result_path}")