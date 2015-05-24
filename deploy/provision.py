# -*- coding: utf-8 -*-

from fabric.api import env, sudo

def provision():
    update_yum()
    install()
    nginx()

def update_yum():
    sudo('yum update -y')

def install():
    sudo('yum -y install git')
    sudo('yum -y install nginx')
    sudo('yum -y install python3')
    sudo('yum -y install python3-pip')
    sudo('python3-pip install virtualenv')

def nginx():
    sudo('systemctl enable nginx')
    sudo('systemctl start nginx')
