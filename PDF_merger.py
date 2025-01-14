import PyPDF2
import os
import sys

merger = PyPDF2.PdfWriter()
directory = input("Enter the directory path of PDFs: ")

for file in os.listdir(directory):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("combinedPDF.pdf")

