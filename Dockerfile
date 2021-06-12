FROM hshar/flaskapp
RUN apt-get update -y && \
    apt-get install -y git && \
    apt-get install -y curl
CMD /bin/bash
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN git clone https://github.com/thomaspauls/flask-app.git
WORKDIR /flask-app
RUN pip3 install -r requirements.txt
CMD [ "python3", "./hello.py" ]
