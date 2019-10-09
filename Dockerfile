FROM        python:alpine3.7
RUN         pip install pipenv
COPY        server/ /app/
WORKDIR     /app
RUN         pipenv install
CMD         pipenv run python ./run.py