FROM python:3.7-alpine
WORKDIR /bot
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python","-u", "bot.py"]