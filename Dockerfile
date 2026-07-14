FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Mengarahkan gunicorn langsung ke file run.py yang baru kita buat
CMD ["gunicorn", "-b", "0.0.0.0:7860", "run:app"]