Provisioning a new site
=======================

## Required packages:
* nginx
* python3
* git
* pip
* virtualenv

e.g., on Fedora 20:
  sudo yum install nginx git python3 python3-pip
  sudo python3-pip install virtualenv


## Nginx Virtual Host config
* see nginx.template.conf and nginx.conf
* replace SERVICE_NAME with, e.g., tddpy
* replace SERVICE_PORT with, e.g., 80


## Systemd job
* see gunicorn-systemd.template.conf
* replace SERVICE_NAME with, e.g., tddpy


## Folder structure
Assume we have a user account at /home/USERNAME
/home/USERNAME
* sites
 - SITENAME
  + database
  + source
  + static
  + virtualenv
