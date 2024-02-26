FROM python:3.10.0-slim-buster

ENV APP_HOME=/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
#Workdir sets the directory for any run,cmd,entrypoint,copy and instructions that follow it in the docker file
WORKDIR $APP_HOME

LABEL maintainer="fullmovies560016@gmail.com"
LABEL youtube="https://www.youtube.com/c/brandzandtutu"
LABEL description="Development image for Real Estate Project"

#prevents python from writing byte code to disk
ENV PYTHONDONTWRITEBYTECODE 1

#python output is transmitted directly to the terminal without being buffered(this allows to display the application output in realtime)
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y build-essential && apt-get install -y libpq-dev && apt-get install -y gettext && apt-get install -y netcat gcc postgresql && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

# Copy application code
#COPY . .

#entrypoint shell script 
COPY ./dk/lo/dj/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//g' /entrypoint.sh
RUN chmod +x /entrypoint.sh

#start script
COPY ./dk/lo/dj/start.sh /start.sh
RUN sed -i 's/\r$//g' /start.sh
RUN chmod +x /start.sh

ENTRYPOINT [ "/entrypoint.sh" ]

