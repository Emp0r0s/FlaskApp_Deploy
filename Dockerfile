#pulls python image
FROM python:3.8-alpine
#copy requirements file to image
COPY ./requirements.txt /app/requirements.txt
#set-up working dir
WORKDIR /app
#install dependencies from requirements.txt
RUN pip install -r requirements.txt
#copy main.py to image
COPY . /app
#run entrypoint and command
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]