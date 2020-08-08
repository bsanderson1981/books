# Pull base image

FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system
#RUN pip install pipenv==2018.11.26 && pipenv install --system
#pipenv==2018.11.26 this fix network error as show on https://github.com/pypa/pipenv/issues/4220
# Copy project
COPY . /code/

#run with >>$ docker build --network=host 
#was getting newwork error on pip install ....  run part 
