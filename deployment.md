# Deployment commands for silly billys

    heroku create "appname"

    git push heroku main

    heroku run bash

    python app.py --detach

Copy environment variables from .env

    heroku config:set ENVIRONMENT_VAR="some variable"

    heroku logs --ps worker