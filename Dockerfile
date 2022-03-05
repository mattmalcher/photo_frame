FROM python:3.9.10-slim-buster

RUN pip install --upgrade pip

# make a non priveliged user
RUN groupadd -g 1000 worker && \
    useradd -r -u 1000 -g worker worker &&\ 
    mkdir /home/worker &&\
    chown worker /home/worker
USER worker

# execute commands in the flask app directory
WORKDIR /usr/src/app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

#Server will reload itself on file changes if in dev mode
ENV FLASK_ENV=development 

# add the worker users bin location to path to avoid warnings
ENV PATH="/home/worker/.local/bin:${PATH}"

# install packages from requirements
COPY --chown=worker:worker requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

CMD ["flask", "run"]