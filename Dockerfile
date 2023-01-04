FROM python:3.9-buster as builder

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /app
WORKDIR /app

RUN pip install -U pip

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu
COPY ./requirements_additional.txt ./requirements_additional.txt
RUN pip install -r ./requirements_additional.txt

FROM python:3.9-slim-buster as production

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libgl1-mesa-dev libopencv-dev

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages/
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn
COPY ./app.py /app/app.py
COPY ./model_download.py /app/model_download.py

WORKDIR /app
RUN python /app/model_download.py

EXPOSE 8080

CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
