# edit document like cover letter using terminal
# save the changes in word file format and pdf 

#import libraries
import datetime                 #import datetime
from docxtpl import DocxTemplate # import the reader
import docx2pdf                  # import the pdf converter 


#initialize the class
class CoverLetterEditor:
    def __init__(self):
        # set the variables
        self.today_date = datetime.datetime.today().strftime("%B %d, %Y")
        self.company_name = ""
        self.company_address = ""
        self.country = ""
        self.job_title = ""

    def set_details(self):
        #take input from the user
        self.company_name = input("Company Name :")
        self.company_address = input("Company Address: ")
        self.country = input("Country: ")
        self.job_title = input("Job Title: ")

    def generate_letter(self):

        context = {
            "today_date": self.today_date,
            "company_name": self.company_name,
            "company_address": self.company_address,
            "country": self.country,
            "job_title": self.job_title,
        }
        #read and render the cover letter
        doc = DocxTemplate("cover_letter.docx")
        doc = render(context)
        #save the cover letter
        doc.save(f"cover_letter_{self.company_name}_{self.job_title}")
        
        #convert it into a pdf format
        docx2pdf.convert(
            f"cover_letter_{self.Company_Name}_{self.job}.pdf",
        )

#Usage
editor = CoverLetterEditor()
editor.set_details()
editor.generate_letter()
