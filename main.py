from reportlab.pdfgen import canvas
from datetime import datetime

def create_pdf(filename, text):
    c = canvas.Canvas(filename)
    c.setFont("Helvetica", 12)

    y = 800  # starting height

    for line in text.split("\n"):
        c.drawString(50, y, line)
        y -= 20  

    c.save()
    print(f"✔ PDF Saved as: {filename}")


print("===== PDF GENERATOR BOT =====")
print("Type your text below. Type 'done' when finished.\n")

content = ""

while True:
    user = input()

    if user.lower() == "done":
        break

    content += user + "\n"

# create filename with time
now = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"GeneratedPDF_{now}.pdf"

# create pdf
create_pdf(filename, content)
