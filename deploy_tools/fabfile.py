#!/usr/bin/env python

from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL = 'https://xirc@bitbucket.org/xirc/tddpy.git'

def deploy():
    #site_folder = '/home/%s/sites/%s' % (env.user, env.host)
    site_folder = '/home/%s/sites/tddpy' % (env.user)
    _get_latest_source(site_folder)
    _create_directory_structure_if_necessary(site_folder)
    _update_settings(site_folder, env.host)
    _update_virtualenv(site_folder)
    _update_static_files(site_folder)
    _update_database(site_folder)

def _get_latest_source(site_folder):
    if exists(site_folder + '/.git'):
        run('cd %s && git fetch' % (site_folder,))
    else:
        run('git clone %s %s' % (REPO_URL, site_folder))
    current_commit = local('git log -n 1 --format=%H', capture=True)
    run('cd %s && git reset --hard %s' % (site_folder, current_commit))

def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ('database', 'static', 'virtualenv'):
        run('mkdir -p %s/%s' % (site_folder, subfolder))

def _update_settings(site_folder, site_name):
    settings_path = site_folder + '/source/superlists/settings.py'
    sed(settings_path, 'DEBUG = True', 'DEBUG = False')
    sed(settings_path,
        'ALLOWED_HOSTS =.+$',
        'ALLOWED_HOSTS = ["%s"]' % (site_name,))
    secret_key_file = site_folder + '/source/superlists/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, "SECRET_KEY = '%s'" % (key,))
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')

def _update_virtualenv(site_folder):
    virtualenv_folder = site_folder + '/virtualenv'
    if not exists(virtualenv_folder + '/bin/pip'):
        run('virtualenv --python=python3 %s' % (virtualenv_folder,))
    run('%s/bin/pip install -r %s/requirements.txt' %
            (virtualenv_folder, site_folder))

def _update_static_files(site_folder):
    run('cd %s/source && ../virtualenv/bin/python manage.py collectstatic --noinput' %
            (site_folder,))

def _update_database(site_folder):
    run('cd %s/source && ../virtualenv/bin/python3 manage.py migrate --noinput' %
            (site_folder,))
