from fpdf import FPDF
import webbrowser


class Bill:
    def __init__(self, amount, peroid):
        self.amount = amount
        self.peroid = peroid


class Flatmates:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / \
            (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))

        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("apple-98.png", w=30, h=30)

        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.peroid, border=0, ln=1)

        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)


the_bill = Bill(amount=120, peroid="April 2023")
john = Flatmates(name="John", days_in_house=20)
marry = Flatmates(name="Marry", days_in_house=25)

print("John pays: ", john.pays(bill=the_bill, flatmate2=marry))
print("Marry pays:", marry.pays(bill=the_bill, flatmate2=john))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)
