FROM python:3.12

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python","main.py","https://www.iana.org/help/example-domains"]
