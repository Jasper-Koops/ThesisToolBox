#!/bin/bash
echo 'activating VitualEnvironment...' 
source ../venv/bin/activate || exit 1

echo 'running migrations...' 
python manage.py migrate || exit 1

echo 'running tests...'
coverage run manage.py test || exit 1

echo 'restarting rabbitmq-server' || exit 1
systemctl stop rabbitmq-server || exit 1
systemctl start rabbitmq-server || exit 1

echo 'restarting supervisor...'
systemctl restart supervisor.service || exit 1

echo 'restarting gunicorn...' 
sudo systemctl restart gunicorn || exit 1

echo 'Server has been deployed, current code coverage:'
coverage report || exit 1
