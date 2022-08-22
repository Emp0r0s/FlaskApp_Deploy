# FlaskApp_Deploy

Install dependencies with "pip install -r requirements.txt"
can be directly be deployed or can be used as container as well

Deploying Process Heroku-
* login in heroku using  " heroku login "
* login to heroku container registry " heroku contianer:login "
* create heroku app " heroku create "
* build and push container image " heroku container:push web "
* Creating container on heroku host " heroku contianer:release web "
* open heroku app " heroku open "
