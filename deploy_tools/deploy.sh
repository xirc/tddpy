#!/usr/bin/env bash

source .deploy
fab deploy --host=${DEPLOY_USER}@${DEPLOY_HOST}
