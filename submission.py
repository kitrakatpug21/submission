import PyPDF2
pdfobj = open("The_Living_World.pdf","rb")
data = PyPDF2.PdfFileReader(pdfobj)
totalpage=data.getNumPages()
pagedata=[]
for i in range(totalpage):
    pagedata.append(data.getPage(i).extractText())

for i in range(totalpage):
    x=pagedata[i]
    x=x.split("Objective Type Questions\n")
    if (len(x) > 1):
        pass
    else:
        x=pagedata[i]
        x=x.split("Ph.011-47623456\n")
    y=x[1].split(".Chapter ")
    x=open("pdftotext.txt","a")
    upload = "Page:"+str(i+1)+" Data-\n"+y[0]+"\n\n"
    x.write(upload)
    x.close()

