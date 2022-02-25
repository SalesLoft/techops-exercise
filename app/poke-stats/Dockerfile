FROM python:3

COPY . .

RUN pip install flask
RUN pip install requests
RUN pip install github3.py
RUN pip install datadog
RUN pip install yaspin

ENTRYPOINT python app.py
