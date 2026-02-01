# 1. Use Python base image
FROM python:3.9-slim

# 2. Set working folder
WORKDIR /app

# 3. Copy the script
COPY app.py .

# 4. Run the script directly (No pip install needed!)
CMD ["python", "app.py"]