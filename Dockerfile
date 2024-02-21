FROM python:3.10

#Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

#Install production dependencies.
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY assets ./
COPY pages62 ./
COPY app62.py ./
COPY aula7_2.py ./
COPY *.pkl ./

EXPOSE 8080 

CMD python aula7_2.py