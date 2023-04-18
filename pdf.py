import pandas as pd
import pdfquery

#read the pdf

pdf = pdfquery.PDFQuery('Resume-MuhammadHaikalNasrizal.pdf')
pdf.load()

pdf.tree.write("haikal.xml",pretty_print=True)
