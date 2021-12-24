FROM python:3.7-alpine
WORKDIR /filewatcher
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python","-u","file_watcher.py"]
