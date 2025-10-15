import sys
import os
import tempfile
from pdf2docx import parse

def convert_pdf_to_docx(pdf_path, docx_path):
    try:
        # Use absolute paths
        pdf_path = os.path.abspath(pdf_path)
        
        # Create the output in a temporary directory (Railway compatible)
        temp_dir = tempfile.gettempdir()
        temp_docx = os.path.join(temp_dir, os.path.basename(docx_path))
        
        print(f"Input PDF: {pdf_path}")
        print(f"Requested output: {docx_path}")
        print(f"Actual output: {temp_docx}")
        
        # Check if input file exists
        if not os.path.exists(pdf_path):
            print(f"Error: Input PDF file not found: {pdf_path}")
            sys.exit(1)
            
        print(f"Input file exists, size: {os.path.getsize(pdf_path)} bytes")
        
        # Convert PDF to DOCX
        parse(pdf_path, temp_docx)
        
        # Check if output file was created
        if os.path.exists(temp_docx):
            file_size = os.path.getsize(temp_docx)
            print(f"File successfully created at: {temp_docx}, size: {file_size} bytes")
            
            # RETURN THE ACTUAL FILE PATH, not the requested one
            return temp_docx
        else:
            print("Error: File was not created in temp location")
            sys.exit(1)
            
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python converter.py <input_pdf> <output_docx>")
        sys.exit(1)
        
    pdf_path = sys.argv[1]
    docx_path = sys.argv[2]
    
    # Get the ACTUAL file path where the file was created
    actual_file_path = convert_pdf_to_docx(pdf_path, docx_path)
    
    # Print ONLY the actual file path (this is what your main app should read)
    print(f"ACTUAL_FILE_PATH:{actual_file_path}")