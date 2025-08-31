document.getElementById('uploadForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const fileInput = document.getElementById('fileInput');
    const textInput = document.getElementById('emailTextInput');
    const resultDiv = document.getElementById('result');
    
    if (fileInput.files.length === 0 && textInput.value.trim() === '') {
        resultDiv.textContent = 'Por favor, selecione um arquivo ou cole um texto.';
        return;
    }

    const formData = new FormData();
    
    if (fileInput.files.length > 0) {
        formData.append('file', fileInput.files[0]);
    } else {
        formData.append('email_text', textInput.value);
    }

    resultDiv.textContent = 'Analisando...';

    try {
        const response = await fetch('/api/process', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error(`Erro na resposta da API: ${response.status}`);
        }

        const data = await response.json();
        
        if (data.classification) {
            resultDiv.textContent = `Resultado: ${data.classification}`;
        } else if (data.error) {
            resultDiv.textContent = `Erro: ${data.error}`;
        } else {
            resultDiv.textContent = 'Resposta inesperada da API.';
        }

    } catch (error) {
        resultDiv.textContent = `Erro: ${error.message}`;
        console.error('Erro:', error);
    }
});