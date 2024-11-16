# import the library to work with pdfs
import PyPDF2
from tkinter import Tk  # this library helps to create a window
from tkinter.filedialog import askopenfilenames, asksaveasfilename

# class to handle PDF merging
class PdfMerger:

    # constructor to initialize with zero initial PDF selections
    def __init__(self):
        self.pdf_files = []

    # method to allow user to select the PDFs 
    def pdf_files_selection(self):
        Tk().withdraw()
        self.pdf_files = askopenfilenames(title='select PDFs', filetypes=[('PDF files', '*.pdf')])
        
    # method to merge selected PDFs
    def merge_pdf(self):
        
        pdf_merge = PyPDF2.PdfMerger()
        for pdf_file in self.pdf_files:
            pdf_merge.append(pdf_file)
        return pdf_merge

    # method to save merged PDFs
    def save_merged(self, merged_pdf):
        
        output_file_path = asksaveasfilename(defaultextension=".pdf", filetypes=[('PDF files', '*.pdf')])
        if output_file_path:
            merged_pdf.write(output_file_path)
            print(f'PDF saved as {output_file_path}')
    # main method to run entire process       
    def run(self):
        self.pdf_files_selection()
        if self.pdf_files:
            merged_pdf = self.merge_pdf()
            self.save_merged(merged_pdf)
            
# create an instance and run the application
if __name__ == "__main__":
    app = PdfMerger()
    app.run()
        
