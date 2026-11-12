FROM python:3.11-slim

WORKDIR /opt/program
RUN pip install --no-cache-dir torch==2.3.1 transformers==4.44.2 flask==3.0.3 gunicorn==22.0.0

# Build with: docker build -f sagemaker/Dockerfile .
COPY model.py /opt/program/model.py
COPY sagemaker/inference.py /opt/program/inference.py

ENV MODEL_ID=distilgpt2
ENV PORT=8080
EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--timeout", "600", "inference:app"]
