#!/usr/bin/env bash

source .env
fab deploy --host=${DEPLOY_USER}@${DEPLOY_HOST} --set=app=tddpy-staging,app_port=8000
