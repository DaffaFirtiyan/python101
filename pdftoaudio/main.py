import pyttsx3
import PyPDF3

pdf = open('pdftoaudio/book.pdf', 'rb')
pdf_reader = PyPDF3.PdfFileReader(pdf)
speaker = pyttsx3.init()
full_text = ""

for page in range(pdf_reader.numPages):
    text = pdf_reader.getPage(page).extractText()
    clean = text.strip().replace('\n', '')
    full_text += clean
    speaker.say(clean)

speaker.save_to_file(full_text, 'audiobook.mp3')
speaker.runAndWait()
speaker.stop()