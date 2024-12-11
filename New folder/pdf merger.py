# import the library to work with pdfs
import PyPDF2
from tkinter import Tk  # this library helps to create a window
from tkinter.filedialog import askopenfilenames, asksaveasfilename

class PdfMerger:
    
    def __init__(self):
        self.pdf_files = []
        
    def pdf_files_selection(self):
        try:
            Tk().withdraw()
            self.pdf_files = askopenfilenames(title='select PDFs', filetypes=[('PDF files', '*.pdf')])
            if len(self.pdf_files) == 0:
                print("No PDFs are selected")
        except Exception as e:
            print(f'error selecting the files: {e}')
            
    def merge_pdf(self):
        try:
            if len(self.pdf_files) == 0:
                print("No PDFs to merge")
                return None
        
            pdf_merge = PyPDF2.PdfMerger()
            for pdf_file in self.pdf_files:
                pdf_merge.append(pdf_file)
            return pdf_merge
        except Exception as e:
            print(f'Error merging PDFs: {e}')
            return None
    
    def save_merged(self, merged_pdf):
        try:
            if merged_pdf == None:
                print('No merged pdfs to save')
        
            output_file_path = asksaveasfilename(defaultextension=".pdf", filetypes=[('PDF files', '*.pdf')])
            if len(output_file_path) > 0:
                merged_pdf.write(output_file_path)
                print(f'PDF saved as {output_file_path}')
        except Exception as e:
            print(f'Error saving the pdf: {e}')
            
    def run(self):
        try:
            self.pdf_files_selection()
            if len(self.pdf_files) > 0:
                merged_pdf = self.merge_pdf()
                self.save_merged(merged_pdf)
        except Exception as e:
            print(f'An error occured: {e}')
            
    
if __name__ == "__main__":
    app = PdfMerger()
    app.run()
        
