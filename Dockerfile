FROM python:3
RUN mkdir /code

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
CMD python testtask/manage.py runserver
COPY . /code/

