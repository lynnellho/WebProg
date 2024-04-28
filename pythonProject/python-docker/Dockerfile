FROM python:3.10-slim-buster

RUN mkdir dockerdjango
WORKDIR /dockerdjango

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r  \requirements.txt

COPY dockerdjango /

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD ["manage.py", "runserver" ]