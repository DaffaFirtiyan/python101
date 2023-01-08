import PyPDF2
import os

path = "pdfMerger\pdf"
output = PyPDF2.PdfMerger()

for file in os.listdir(path):
    if file.endswith(".pdf"):
        absfile = os.path.join(path, file)
        print(absfile)
        output.append(absfile)
    output.write("pdfMerger\combinedFile.pdf")
output.close()