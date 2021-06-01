import pyttsx3
import PyPDF2

# Open the pdf file with in-built function open
book = open(
    'Data/Flask_Web_Development_Developing.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(book)

# Get total number of pages
pages = pdfReader.numPages

# Initialize the Text to Speach Engine
engine = pyttsx3.init()

# from Start to end of all the pages in the PDF,
# Get text from each page and convert the extracted text to speach
for i in range(0, pages-1):
    page = pdfReader.getPage(i)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()
