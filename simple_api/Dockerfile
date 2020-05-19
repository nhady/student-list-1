FROM python:2.7-stretch
MAINTAINER 227720
COPY / /
RUN apt-get update -y && apt-get install python-dev python3-dev libsasl2-dev python-dev libldap2-dev libssl-dev -y
RUN pip install flask flask_httpauth flask_simpleldap python-dotenv
RUN mkdir /data
VOLUME /data
COPY /student_age.json /data/student_age.json
EXPOSE 1023
CMD [ "python", "./student_age.py" ]
