# import the library to work with pdfs
import PyPDF2
from tkinter import Tk  # this library helps to create a window
from tkinter.filedialog import askopenfilenames, asksaveasfilename

class PdfMerger:
    
    def __init__(self):
        self.pdf_files = []
        
    def pdf_files_selection(self):
        Tk().withdraw()
        self.pdf_files = askopenfilenames(title='select PDFs', filetypes=[('PDF files', '*.pdf')])
        
    def merge_pdf(self):
        
        pdf_merge = PyPDF2.PdfMerger()
        for pdf_file in self.pdf_files:
            pdf_merge.append(pdf_file)
        return pdf_merge
    
    def save_merged(self, merged_pdf):
        
        output_file_path = asksaveasfilename(defaultextension=".pdf", filetypes=[('PDF files', '*.pdf')])
        if output_file_path:
            merged_pdf.write(output_file_path)
            print(f'PDF saved as {output_file_path}')
            
    def run(self):
        self.pdf_files_selection()
        if self.pdf_files:
            merged_pdf = self.merge_pdf()
            self.save_merged(merged_pdf)
            
    
if __name__ == "__main__":
    app = PdfMerger()
    app.run()
        
