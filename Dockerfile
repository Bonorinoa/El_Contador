# El_Contador/Dockerfile

FROM python:3.9-slim

EXPOSE 8501

WORKDIR /El_Contador

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install twilio pandas streamlit

ENTRYPOINT ["streamlit", "run", "Personal_Accountant.py", "--server.port=8501", "--server.address=0.0.0.0"]