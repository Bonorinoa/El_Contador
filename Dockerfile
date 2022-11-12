# El_Contador/Dockerfile

FROM python:3.9

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

RUN pip3 install streamlit

EXPOSE 5000

COPY . /app

ENTRYPOINT ["streamlit", "run", "Alfred.py", "--server.port=5000", "--server.address=0.0.0.0"]

CMD ["app.py"]