from transformers import pipeline

def classify_email(email_content):
    try:
        classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli"
        )
        
        candidate_labels = [
            "trabalho e produtividade",
            "assuntos pessoais", 
            "reuniões e projetos",
            "entretenimento",
            "tarefas profissionais",
            "conversas casuais"
        ]
        
        result = classifier(email_content, candidate_labels)
        
        top_label = result['labels'][0]
        confidence = result['scores'][0]
        
        productive_labels = [
            "trabalho e produtividade",
            "reuniões e projetos",
            "tarefas profissionais"
        ]

        if top_label in productive_labels and confidence > 0.3:
            return "Categoria: Produtivo! " \
            "Sugestão: Olá, e-mail obrigado pelo e-mail! Retornaremos o mais breve possível"
        else:
            return "Categoria: Improdutivo! " \
                "Sugestão: Olá, Obrigado pela mensagem!"
            
    except Exception as e:
        print(f"Erro na classificação: {e}")
        return "inconclusivo"