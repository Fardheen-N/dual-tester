FROM ubuntu:latest
LABEL authors="Fardheen.n"

RUN apt-get update && apt-get install -y python3 python3-pip wget sudo curl jq python3-venv
RUN apt-get clean

COPY requirements.txt .

RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r requirements.txt

RUN mkdir -p /apps
WORKDIR /app
COPY . .

EXPOSE 8000
ENTRYPOINT ["top", "-b"]
CMD ["pytest", "-m login"]