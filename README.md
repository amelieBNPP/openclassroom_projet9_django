# openclassroom - projet9 - application Django

_Owner: [Amélie](https://github.com/ameliebnpp)_

## Developpement guide

### Installation

1. Create the virtual environement and activate it:
```bash
python -m venv .venv
source .venv/bin/activate
```
*The virtual environement is created only one time, however, it is activate each time we start to develop.*

2. Clone the project:

```bash
git clone --recursive git@github.com:/amelieBNPP/openclassroom_projet9_django && cd openclassroom_projet9_django
```
*Clone only one time the project.*

### Dependencies

Install dependencies :

```bash
pip install -r requirements.txt
```
*Install dependancies each time we develop on this project.*

### Run server

Server can be run using the following commands:
```bash
python manage.py runserver
```

### Data base management

Three tables have been set. Launch postgresql with the following command: 
```bash
sudo -u postgres psql
```

To create new user, run the following command:
```bash
CREATE USER name WITH ENCRYPTED PASSWORD 'password';
```
An easyest way to manage database is to go throught [PgAdmin4](https://www.pgadmin.org/download/)

| key commands | descriptions | 
|:----------:|:-------------:|
| ctr D| quit SQL |
| \l| display table |
| \d tablename | table description |

### Django

Django is an open source framework write in python that allow to create complexes website easily.

1. shell access & database communication
```
python manage.py shell
from database.models import Ticket

```