FROM python:3.7-alpine
WORKDIR /filewatcher
COPY . /filewatcher
RUN pip install -r requirements.txt
CMD ["python","file_watcher.py"]