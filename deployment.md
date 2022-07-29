# Deployment commands for silly billys

    heroku create "appname"

    git push heroku main

Copy environment variables from .env

    heroku config:set ENVIRONMENT_VAR="some variable"