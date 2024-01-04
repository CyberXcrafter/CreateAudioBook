#pip install PyPDF2
#pip install pyttsx3

import PyPDF2
import pyttsx3

# Read the PDF by specifying the path in your computer
pdf_path = 'Sample.pdf'
pdfReader = PyPDF2.PdfReader(pdf_path)

# Get the handle to the speaker
speaker = pyttsx3.init()

text = ''
# Split the pages and read one by one
for page_num in range(len(pdfReader.pages)):
    page = pdfReader.pages[page_num]
    text += page.extract_text()

    # Speak the text of each page
    speaker.say(page.extract_text())
    speaker.runAndWait()

# Stop the speaker after completion
speaker.stop()

# Save the entire text as an audiobook at the specified path
engine = pyttsx3.init()
engine.save_to_file(text, 'audio.mp3')
engine.runAndWait()
