# 📧 E-mail classifier

# Sistema inteligente de classificação de emails utilizando Machine Learning e processamento de linguagem natural.

## 🚀 Sobre o Projeto

# O **Email Classifier** é uma aplicação web desenvolvida em Python que utiliza modelos de Machine Learning da Hugging Face para classificar automaticamente o conteúdo de emails. O sistema permite upload de arquivos (PDF/TXT) ou entrada direta de texto, processando e categorizando o conteúdo de forma inteligente e retornando uma sugestão de resposta ao e-mail. #

## Tecnologias Utilizadas

- **Backend**: Python, Flask
- **Machine Learning**: Hugging Face Transformers
- **Processamento de Arquivos**: PyMuPDF (fitz) para PDFs
- **Frontend**: HTML, CSS, JavaScript
- **Arquitetura**: Clean Architecture com separação de responsabilidades

## 📁 Estrutura do Projeto
```
email-classifier/
├── app/
│   ├── __init__.py              # Configuração da aplicação Flask
│   ├── domain/
│   │   └── entities.py          # Entidades de domínio
│   ├── handlers/
│   │   ├── pdf_handler.py       # Processamento de arquivos PDF
│   │   └── txt_handler.py       # Processamento de arquivos TXT
│   ├── services/
│   │   └── hf_service.py        # Serviço de classificação com Hugging Face
│   └── web/
│       ├── api.py               # Endpoints da API REST
│       └── routes.py            # Rotas da interface web
├── templates/
│   └── index.html               # Interface do usuário
├── static/                      # Arquivos estáticos (CSS, JS)
└── run.py                       # Ponto de entrada da aplicação
```

## Funcionalidades

- **Upload de Arquivos**: Suporte para arquivos PDF e TXT
- **Entrada de Texto**: Classificação direta de texto digitado
- **Processamento Inteligente**: Extração automática de conteúdo de PDFs
- **API REST**: Endpoints para integração com outras aplicações
- **Interface Responsiva**: Design moderno e intuitivo
- **Tratamento de Erros**: Validação robusta de entrada e tipos de arquivo

##  Como Executar
### Pré-requisitos
```bash
Python 3.8+
pip
```

### Instalação
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/email-classifier.git
cd email-classifier

# Instale as dependências
pip install flask PyMuPDF transformers torch

# Execute a aplicação
python run.py
```

### Acesso
- **Interface Web**: `http://localhost:5000`
- **API**: `http://localhost:5000/api/process`

## 📊 API Reference

### POST /api/process

Classifica o conteúdo de um email.

**Parâmetros:**
- `file`: Arquivo PDF ou TXT (opcional)
- `email_text`: Texto direto para classificação (opcional)

**Resposta:**
```json
{
  "classification": "categoria_identificada"
}
```

**Exemplo de uso:**
```bash
curl -X POST \
  -F "file=@email.pdf" \
  http://localhost:5000/api/process
```

##  Arquitetura

# O projeto segue princípios de **Clean Architecture**:

- **Domain**: Entidades de negócio (`EmailContent`)
- **Handlers**: Processamento específico por tipo de arquivo
- **Services**: Lógica de classificação com ML
- **Web**: Camada de apresentação (API + Interface)

## 🧠 Machine Learning

# A classificação é realizada utilizando modelos pré-treinados da **Hugging Face**
- Alta precisão na classificação
- Processamento de linguagem natural avançado
- Modelos state-of-the-art em NLP

## 🎯 Diferenciais Técnicos

- **Modularidade**: Código organizado em camadas bem definidas
- **Extensibilidade**: Fácil adição de novos tipos de arquivo
- **Robustez**: Tratamento de encoding UTF-8 e Latin-1
- **Performance**: Processamento eficiente de arquivos PDF
- **Usabilidade**: Interface intuitiva para usuários finais

## 🚀 Próximos Passos

- [ ] Implementar autenticação de usuários
- [ ] Adicionar suporte para mais formatos (DOCX, RTF)
- [ ] Dashboard com métricas de classificação
- [ ] API de histórico de classificações
- [ ] Testes automatizados (pytest)

## 👨‍💻 Desenvolvedor

**[Lucas de Freitas Farias]**
# Estudante de análise e desenvolvimento de sistemas
- 💼 LinkedIn: [www.linkedin.com/in/lucas-de-freitas-farias/]
- 🐱 GitHub: [https://github.com/lucasffarias95]
- 📧 Email: [lucasffarias95@gmail.com]

---

*Projeto desenvolvido como parte do portfólio*