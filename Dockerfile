FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Instala dependências de build e runtime
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    ffmpeg \
    libopus0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos da aplicação
COPY . .

# Atualiza o pip e instala dependências do projeto
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Executa o bot
CMD ["python", "main.py"]
