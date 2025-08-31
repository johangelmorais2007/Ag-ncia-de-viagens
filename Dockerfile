FROM python:3.11-slim

# Configura diretório de trabalho
WORKDIR /app

# Copia requirements (corrigido o nome do arquivo)
COPY requirements.txt /tmp/requirements.txt

# Instala dependências do sistema + Python libs
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /var/lib/apt/lists/*

# Copia o código do projeto
COPY . /app

# Expõe a porta
EXPOSE 8000

# Roda como usuário não root
RUN useradd -m django-user
USER django-user

# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
