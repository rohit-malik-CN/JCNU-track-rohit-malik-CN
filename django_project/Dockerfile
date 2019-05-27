FROM python:3
WORKDIR /app
COPY . /app/
RUN pip3 install -r requirements.txt
RUN chmod u+x entrypoint.sh
RUN chmod u+x flaskserver.sh
EXPOSE 8080
EXPOSE 8000
RUN pip3 install -r python-flask-server/requirements.txt
CMD sh entrypoint.sh
