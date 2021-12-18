FROM python:3.7-alpine
WORKDIR /bot
COPY . /bot
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]