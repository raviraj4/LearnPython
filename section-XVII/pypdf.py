import pypdf
path = "pathtofile"
f = open(path, 'rb')
pdf = pypdf.PdfFileReader(f)
pdf.numPages # number of pages
page_1 = pdf.getPage(0)
text = pdf.extractText() 
f.close()