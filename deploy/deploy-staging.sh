#!/usr/bin/env bash

source .env
fab -f deploy.py deploy --host=${DEPLOY_USER}@${DEPLOY_HOST} --set=app=tddpy-staging,app_port=8000
