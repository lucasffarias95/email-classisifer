from flask import request, jsonify, Blueprint
from app.handlers.txt_handler import handle_txt
from app.handlers.pdf_handler import handle_pdf
from app.services.hf_service import classify_email

api = Blueprint('api', __name__)

@api.route('/process', methods=['POST'])
def process():
    content_as_string = ""

    if 'file' in request.files and request.files['file'].filename != '':
        uploaded_file = request.files['file']
        file_extension = uploaded_file.filename.split('.')[-1]
        
        if file_extension == 'txt':
            email_content = handle_txt(uploaded_file)
            content_as_string = email_content.content
        elif file_extension == 'pdf':
            email_content = handle_pdf(uploaded_file)
            content_as_string = email_content.content
        else:
            return jsonify({'error': 'Unsupported file type'}), 400
    
    elif 'email_text' in request.form and request.form['email_text'].strip() != '':
        content_as_string = request.form['email_text']
        
    else:
        return jsonify({'error': 'No file or text found in the request'}), 400

    if content_as_string:
        classification = classify_email(content_as_string)
        return jsonify({'classification': classification})
        
    return jsonify({'error': 'Não foi possível extrair o conteúdo'}), 400