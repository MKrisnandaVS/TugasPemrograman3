# Gunakan base image Python
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy file ke container
COPY . /app

# Install dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Jalankan aplikasi
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
