FROM python
WORKDIR /code
COPY ./app /code/app
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt
CMD ["python", "app.create_db.py"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "20774"]