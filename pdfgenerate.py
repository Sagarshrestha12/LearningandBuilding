from fpdf import FPDF
def create_pdf(txt):
    id,name,math,SCIENCE,OPT_MATH,ENGLISH,OOP,PERCENT,status=txt
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
    Math_=    "Math                          "+str(math)
    pdf.cell(200,10,txt=Math_,ln=4,align='L')
    SCIENCE_= "SCIENCE                  "+str(SCIENCE)
    pdf.cell(200,10,txt=SCIENCE_,ln=5,align='L')
    OPT_MATH_="OPT_MATH              "+str(OPT_MATH)
    pdf.cell(200,10,txt=OPT_MATH_,ln=6,align='L')
    ENGLISH_= "ENGLISH                  "+str(ENGLISH)
    pdf.cell(200,10,txt=ENGLISH_,ln=7,align='L')
    OOP_=     "OOP                          "+str(OOP)
    pdf.cell(200,10,txt=OOP_,ln=8,align='L')
    blank_="                "+str()
    pdf.cell(200,10,txt=blank_,ln=9,align='L')
    PERCENT_="PERCENT                "+str(PERCENT)
    pdf.cell(200,10,txt=PERCENT_,ln=10,align='L')
    status_="STATUS               "+str(status)
    pdf.cell(200,10,txt=status_,ln=10,align='L')    
    id_=str(id)
    id_=id_ + ".pdf"
    pdf.output(id_)

