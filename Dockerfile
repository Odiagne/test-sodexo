# We can't use Alpine cause we need Sqlalchemy -> mysql -> gcc, so it's not worth
FROM python:3.7.0-stretch

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY . /app
WORKDIR /app/scripts/
EXPOSE 80
RUN  python3 -m unittest test_functions
CMD python3 clustering.py