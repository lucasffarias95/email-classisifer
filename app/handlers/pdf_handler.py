import fitz
from app.domain.entities import EmailContent

def handle_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read())

    full_text = []

    for page in doc:
      full_text.append(page.get_text())

    email_content = '\n'.join(full_text)

    return EmailContent(content=email_content)