# Importing Libraries
# Importing Google Text to Speech library
from gtts import gTTS

# Importing PDF reader PyPDF2
from PyPDF2 import PdfReader

# Open file Path
pdf_File = open('input.pdf', 'rb')

# Create PDF Reader Object
pdf_Reader = PdfReader(pdf_File)
count = len(pdf_Reader.pages)  # counts number of pages in pdf
textList = []

# Extracting text data from each page of the pdf file
for i in range(count):
    try:
        page = pdf_Reader.pages[i]
        textList.append(page.extract_text())
    except:
        pass

# Converting multiline text to single line text
textString = " ".join(textList)

print(textString)

# Set language to english (en)
language = 'en'

# Call GTTS
myAudio = gTTS(text=textString, lang=language, slow=False)

# Save as mp3 file
myAudio.save("Audio.mp3")
