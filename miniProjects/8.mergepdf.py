'''
Write a program to manipulate pdf files using pyPDF.
your program should be able to merge multiple pdf files into a single pdf file.
You are welcome to add more functionalities.
'''
from PyPDF2 import PdfMerger
import os

def merge_pdfs(pdf_list, output_name):
    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)
        print(f"Added: {pdf}")

    merger.write(output_name)
    merger.close()
    print(f"Merged PDF saved as: {output_name}")

if __name__ == "__main__":
    # List of PDF files to merge
    pdf_files = [file for file in os.listdir() if file.endswith('.pdf')]
    
    if len(pdf_files) < 2:
        print("Need at least two PDF files to merge.")
    else:
        output_pdf = "merged_output.pdf"
        merge_pdfs(pdf_files, output_pdf)
        