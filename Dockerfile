FROM python:3.8

WORKDIR .
COPY ./requirements.txt ./requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

RUN pip uninstall --yes werkzeug
RUN pip install -v https://github.com/pallets/werkzeug/archive/refs/tags/2.0.3.tar.gz

COPY ./app.py ./app.py
COPY ./utils.py ./utils.py
COPY ./insurance.csv ./insurance.csv

CMD ["python","app.py"]