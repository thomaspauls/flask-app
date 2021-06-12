FROM hshar/flaskapp
RUN apt-get update -y && \
    apt-get install -y git
RUN git clone https://github.com/thomaspauls/flask-app.git
WORKDIR /flask-app
RUN pip3 install -r requirements.txt
CMD [ "python3", "./hello.py" ]
