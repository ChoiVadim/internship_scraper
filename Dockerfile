FROM python:3.11

WORKDIR /telegram_bot

# Copy requirements.txt first to leverage Docker's caching mechanism
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the command to run your application
CMD ["python", "bot.py"]
