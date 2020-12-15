FROM python:3.6-slim
COPY /webapp /app
WORKDIR /app
RUN pip install -r requirements.txt && python -m nltk.downloader all && chmod a+x run.sh
CMD ["./run.sh"]