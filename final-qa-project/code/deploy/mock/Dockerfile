FROM python:3

WORKDIR /src/

RUN pip install --no-cache-dir flask

COPY . /src/

EXPOSE 5000

CMD ["python", "/src/mock_server.py"]