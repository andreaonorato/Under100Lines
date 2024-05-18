import requests
from bs4 import BeautifulSoup
from docx import Document

def extract_text_from_webpage(url):
    text = ""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        print("Response status code:", response.status_code)  # Debug print to see response status code
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find all paragraphs and concatenate the text
            paragraphs = soup.find_all('p')
            for paragraph in paragraphs:
                text += paragraph.get_text() + '\n'
    except Exception as e:
        print(f"Error extracting text from webpage: {e}")
    return text

def create_docx_from_text(text, output_docx_path):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_docx_path)


url = "https://www.thelocal.dk/20230216/reader-question-what-are-the-rules-on-international-money-transfers-to-and-from-denmark"
output_docx_path = "output.docx"

text = extract_text_from_webpage(url)
print("Extracted text:", text)  # Debug print to see if text is extracted

if text.strip():
    print("Extracted text:", text[:100])  # Print first 100 characters of extracted text
    create_docx_from_text(text, output_docx_path)
    print("DOCX file created successfully.")
else:
    print("No text extracted from the webpage.")
