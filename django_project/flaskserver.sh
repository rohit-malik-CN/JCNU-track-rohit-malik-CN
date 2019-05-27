#! /bin/sh
cd python-flask-server
pip3 install -r requirements.txt
python3 -m swagger_server 0.0.0.0:8080
