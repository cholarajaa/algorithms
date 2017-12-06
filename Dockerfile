FROM python:3.6

WORKDIR /code
COPY . /code

RUN pip install -r requirements.txt

CMD flake8
CMD py.test -vsx tests/ --cov algorithms/ --no-cov-on-fail
CMD bash <(curl -s https://codecov.io/bash)