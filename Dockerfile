FROM nikolaik/python-nodejs:latest

# build environment, prod as default
ARG env=prod

WORKDIR /code

# setting up Python - server
RUN mkdir /code/server
COPY server/requirements.txt /code/server
RUN pip install -r /code/server/requirements.txt

# setting up Angular - client
# note: For a github release, this step will be erased entirely
# and nginx will use the included /dist folder to serve files instead
# of building it from scratch every time
RUN mkdir /code/web
COPY . /code
COPY web/package.json /code/web
WORKDIR /code/web
RUN yarn global add @angular/cli
RUN yarn install

# For some reason this creates some issues because of binaries
# if everything is ok it just ends up being a quick intermediate step
RUN npm rebuild node-sass

# Building client
WORKDIR /code/web
RUN ng build --$env

# Installing Linux dependencies
# RUN add-apt-repository http://archive.ubuntu.com/ubuntu/ universe
RUN apt-get update
RUN apt-get install vlc -y

EXPOSE 10000

# Running the server
WORKDIR /code/server
CMD python app.py
