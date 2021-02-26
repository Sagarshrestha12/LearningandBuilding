from fpdf import FPDF
def create_pdf(txt):
    id,name,math=txt
    pdf =FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=15)
    pdf.cell(200,10,txt="KATHFORD INTERNATIONAL COLLEGE OF ENGINEERING AND MANAGEMENT",
    ln =1,align='C')
    name="Name :"+name
    pdf.cell(200,10,txt=name,ln=2,align='L')
    pdf.cell(200,10,txt="Bachelor's in Engineering",ln=2,align='L') 
    pdf.cell(200,10,txt="     ",ln=2,align='c')   
    pdf.cell(200,10,txt="Subjects          Marks_obtained",ln=3,align='L')
    Math_="Math                "+str(math)
    pdf.cell(200,10,txt=Math_,ln=4,align='L')
    id_=str(id)
    id_=id_ + ".pdf"
    pdf.output(id_)

