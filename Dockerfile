FROM public.ecr.aws/docker/library/python:3.13

RUN mkdir -p /app
COPY ./main.py /app/
COPY ./mylib /app/mylib/
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --verbose --upgrade -r /app/requirements.txt
WORKDIR /app
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]