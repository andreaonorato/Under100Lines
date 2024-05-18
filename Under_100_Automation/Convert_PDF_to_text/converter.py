from PyPDF2 import PdfReader

def pdf_to_text(pdf_path, output_path):
    """Convert PDF to text and save the text to a file."""
    with open(pdf_path, 'rb') as f:
        # Create PDF reader object
        pdf_reader = PdfReader(f)
        
        # Initialize empty string to store text
        text = ''
        
        # Iterate through each page of the PDF
        for page in pdf_reader.pages:
            # Extract text from the page
            text += page.extract_text()
    
    # Write extracted text to a text file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

# Example usage
pdf_to_text('input.pdf', 'output.txt')
