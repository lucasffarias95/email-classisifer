from app.domain.entities import EmailContent

def handle_txt(uploaded_file):
    try:
        content_as_string = uploaded_file.read().decode('utf-8')
    except UnicodeDecodeError:
        uploaded_file.seek(0)
        content_as_string = uploaded_file.read().decode('latin-1')
    
    return EmailContent(content=content_as_string)