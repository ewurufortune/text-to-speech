import pyttsx3
import PyPDF2
import tkinter as tk
from tkinter import filedialog

def open_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        read_pdf(file_path)

def read_pdf(file_path):
    # Open the selected PDF file
    pdf_file = open(file_path, 'rb')

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Iterate through each page in the PDF
    for page_num in range( len(pdf_reader.pages)):
        # Extract text from the current page
        page = pdf_reader.pages[page_num]
        text = page.extract_text()

        # Speak the extracted text
        engine.say(text)
        engine.runAndWait()

    # Close the PDF file
    pdf_file.close()

    # Shutdown the text-to-speech engine
    engine.stop()

# Create a Tkinter window
root = tk.Tk()
root.title("PDF to Speech Converter")

# Create a button to open the PDF file dialog
open_button = tk.Button(root, text="Open PDF", command=open_pdf)
open_button.pack()

# Start the Tkinter main loop
root.mainloop()
