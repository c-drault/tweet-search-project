FROM python:3.6-slim
COPY /webapp /app
WORKDIR /app
RUN pip install -r requirements.txt && python -m nltk.downloader all && chmod a+x run.sh

EXPOSE 5000
EXPOSE 8010

CMD ["./run.sh"]