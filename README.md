# M&M Soluções Inovadoras - Módulo Cérebro (IA) 🧠

Este é o microsserviço de inteligência artificial da **M&M Soluções Inovadoras**. Ele funciona de forma agnóstica e isolada das regras de negócio, atuando como o "sócio virtual" técnico e estratégico do ecossistema. A API é multimodal, sendo capaz de processar requisições tanto em formato de **texto** quanto de **áudio** (voz) de forma transparente.

## 🛠️ Tecnologias e Bibliotecas
*   **Python 3.12+** (Linguagem base do ecossistema de IA)
*   **FastAPI** (Framework web assíncrono de alta performance)
*   **Uvicorn** (Servidor ASGI para rodar a aplicação local e em produção)
*   **Google GenAI SDK** (Integração direta com o modelo Gemini 2.5 Flash)
*   **Python Dotenv** (Gerenciamento seguro de variáveis de ambiente)

## 📐 Arquitetura do Fluxo de Dados
1. O Frontend (**Next.js / Flutter**) ou o Backend Central (**Java Spring Boot**) dispara uma requisição HTTP POST contendo texto ou um arquivo de áudio (`.mp3`, `.wav`, `.m4a`).
2. O FastAPI recebe os dados de forma assíncrona na rota `/api/brain`.
3. Se houver áudio, o arquivo binário é enviado diretamente para a API multimodal do Google.
4. O texto/áudio é processado junto ao *System Prompt* que define a personalidade técnica e corporativa do sócio.
5. A resposta retorna estruturada em formato JSON (Código 200).

## 🚀 Como Rodar o Projeto Localmente

### 1. Pré-requisitos
Certifique-se de ter o Python 3.12 instalado na máquina e a sua chave de API do Google AI Studio em mãos.

### 2. Configurar o Ambiente Virtual
Clone o repositório, acesse a pasta raiz do projeto e crie o ambiente isolado:
```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente (Windows)
.\venv\Scripts\Activate.ps1

# Ativar o ambiente (Linux/Mac)
source venv/bin/activate
```

### 3. Instalar as Dependências
Com a `venv` ativa, instale os pacotes listados no arquivo de portabilidade:
```bash
pip install -r requirements.txt
```

### 4. Variáveis de Ambiente
Crie um arquivo chamado `.env` na raiz da pasta `mm-cerebro` e adicione a sua credencial do Gemini:
```text
GEMINI_API_KEY=AIzaSyA_SuaChaveRealDoGoogleAqui
```

### 5. Iniciar o Servidor
Execute o Uvicorn para ligar a API com suporte a recarregamento automático (*hot-reload*):
```bash
uvicorn main:app --reload
```
O servidor estará online e disponível no endereço: `http://127.0.0.1:8000`

## 🧪 Testando a API (Interface Gráfica)
O FastAPI gera automaticamente a documentação interativa do Swagger. Com o servidor rodando, acesse no seu navegador:
*   **Interface Swagger:** `http://127.0.0`

Abra o endpoint `POST /api/brain`, clique em **"Try it out"**, envie um texto ou selecione um arquivo de áudio gravado e clique em **"Execute"** para ver a resposta do cérebro.

---
💡 *Nota de Expansão: No futuro, a camada de banco de dados híbrido (PostgreSQL + pgvector) para memória de longo prazo será acoplada diretamente a este microsserviço, mantendo o ecossistema Java e as interfaces de usuário totalmente intactas.*
