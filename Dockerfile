FROM python:3.11-slim

# Install ffmpeg (required for yt-dlp)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot files
COPY telegram_video_bot.py .

# Create directories for data persistence
RUN mkdir -p /app/data

# Run bot
CMD ["python", "telegram_video_bot.py"]
