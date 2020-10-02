#!/bin/bash

apt-get update
apt-get -y install python3 python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3-venv python3-virtualenv
python3 -m pip install -r ./requirements.txt --upgrade
