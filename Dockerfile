FROM python:3.10.13-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN apt update && apt upgrade -y

RUN apt install libgomp1

RUN pipenv install --system --deploy

COPY ["streamlit_app.py", "percent_helpful_model.pickle", "./"]

EXPOSE 5000

ENTRYPOINT ["streamlit", "run", "--server.port", "5000", "streamlit_app.py"]