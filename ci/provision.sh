#!/usr/bin/env bash

# Install latest Jenkins
wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -
echo deb http://pkg.jenkins-ci.org/debian binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list
sudo apt-get update
sudo apt-get install jenkins

# Install a few other dependencies
sudo apt-get install git firefox python3 python-virtualenv xvfb

# Install nodejs and phantomjs for test javascript
sudo add-apt-repository -y ppa:chris-lea/node.js
sudo apt-get update
sudo apt-get install nodejs
sudo apt-get install phantomjs
