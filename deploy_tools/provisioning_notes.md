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
* see nginx.template.conf
* replace SITENAME with, e.g., staging.mydomain.com


## Systemd job
* see gunicorn-systemd.template.conf
* replace SITENAME with, e.g., staging.mydomain.com


## Folder structure
Assume we have a user account at /home/username
/home/username
* sites
 - SITENAME
  + database
  + source
  + static
  + virtualenv
