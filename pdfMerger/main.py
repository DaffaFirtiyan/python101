import PyPDF2
import sys
import os

path = "pdfMerger/pdfFiles"
merger = PyPDF2.PdfMerger()

for file in os.listdir(path):
    if file.endswith(".pdf"):
        merger.append(file, path)
    merger.write("combinedFiles", path)

merger.close()