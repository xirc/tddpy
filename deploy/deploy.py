#!/usr/bin/env python

import random

from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run, sudo

SERVICE_NAME = 'tddpy'
SERVICE_PORT = '80'

def deploy():
    site_folder = '/home/%s/sites/%s' % (env.user, SERVICE_NAME)
    _set_permission(env.user)
    _get_latest_source(site_folder)
    _create_directory_structure_if_necessary(site_folder)
    _update_settings(site_folder, env.host)
    _update_virtualenv(site_folder)
    _update_static_files(site_folder)
    _update_database(site_folder)
    _update_systemd_conf(site_folder, SERVICE_NAME)
    _update_nginx_conf(site_folder, SERVICE_NAME, SERVICE_PORT)

def _set_permission(user):
    sudo('usermod -a -G xirc nginx')
    sudo('chmod 750 /home/{}'.format(user))

def _get_latest_source(site_folder):
    if exists(site_folder + '/.git'):
        run('cd %s && git fetch' % (site_folder,))
    else:
        repo_url = local(
            "git remote -v | grep deploy | uniq | awk -e '{print $2}'",
            capture=True)
        run('git clone %s %s' % (repo_url, site_folder))
    current_commit = local('git log -n 1 --format=%H', capture=True)
    run('cd %s && git reset --hard %s' % (site_folder, current_commit))

def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ('database', 'static', 'virtualenv'):
        run('mkdir -p %s/%s' % (site_folder, subfolder))

def _update_settings(site_folder, site_name):
    settings_path = site_folder + '/source/superlists/settings.py'
    sed(settings_path, 'DEBUG = True', 'DEBUG = False')
    sed(settings_path, 'DOMAIN = "localhost"', 'DOMAIN = "%s"' % (site_name,))
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

def _update_systemd_conf(site_folder, service_name):
    template_path = site_folder + '/deploy/gunicorn.template.service'
    systemd_service_name = 'gunicorn-{}.service'.format(service_name)
    service_path = '/etc/systemd/system/{}'.format(systemd_service_name)
    tmp_path = site_folder + '/deploy/{}'.format(systemd_service_name)

    run('cp -a {} {}'.format(template_path, tmp_path))
    sed(tmp_path, '\{SERVICE_NAME\}', service_name)
    sudo('mv {} {}'.format(tmp_path, service_path))

    sudo('systemctl daemon-reload')
    sudo('systemctl restart {}'.format(systemd_service_name))

def _update_nginx_conf(site_folder, service_name, service_port):
    sudo('cp -a {}/deploy/nginx.conf /etc/nginx/nginx.conf'.format(site_folder))

    template_path = site_folder + '/deploy/nginx.template.conf'
    conf_path = '/etc/nginx/conf.d/{}.conf'.format(service_name)
    tmp_path = site_folder + '/deploy/{}.conf'.format(service_name)

    run('cp -a {} {}'.format(template_path, tmp_path))
    sed(tmp_path, '\{SERVICE_NAME\}', service_name)
    sed(tmp_path, '\{SERVICE_PORT\}', service_port)
    sudo('mv {} {}'.format(tmp_path, conf_path))

    sudo('systemctl reload nginx')
    sudo('firewall-cmd --permanent --add-port={}/tcp'.format(service_port))
    sudo('firewall-cmd --reload')
