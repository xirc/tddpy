#!/usr/bin/env bash

source .env
fab deploy --host=${DEPLOY_USER}@${DEPLOY_HOST} --set=app=tddpy,app_port=80
