# training_stats [![Build Status](https://travis-ci.org/vinntreus/training_stats.svg?branch=master)](https://travis-ci.org/vinntreus/training_stats)

## Setup on local dev
```shell
make db-up
make env
source ./settings
source ./env/bin/activate
```

## Start web
With gunicorn
```shell
make web
```
With flask development server
```shell
python run_web.py
```
