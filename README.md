# openclassroom - projet9 - application Django

_Owner: [Amélie](https://github.com/ameliebnpp)_

## Developpement guide

### Installation

1. Clone the project:

```bash
git clone --recursive git@github.com:/amelieBNPP/openclassroom_projet9_django && cd openclassroom_projet9_django
```
*Clone only one time the project.*

2. Create the virtual environement and activate it:
```bash
python -m venv .venv
source .venv/bin/activate
```
*The virtual environement is created only one time, however, it is activate each time we start to develop.*

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
An easyest way to manage database is to run the server and go throught [DjangoAdministration](
    http://127.0.0.1:8000/admin/)

| key commands | descriptions | 
|:----------:|:-------------:|
| showmigrations | show the list of migrations and their states |
| makemigrations | create new migration with updates |
| migrate | execute the migration |

## LiteReview website
### Stack developement

This project is developped in python with Django framework.
Django is an open source framework write in python that allow to create complexes website easily.
- Design have been developped through the free template [sb admin 2](https://startbootstrap.com/theme/sb-admin-2)
- The website is responsive and can be used for computer or smartphone screen

### About website
The aim of this project is to develop a website **LITEREVIEW** that allow to ask review about a book.
1. User can register/login
2. User can create a ticket to request a review
3. User can add review about a book
4. user can follow others users

### Preview

![Login](/login.png)
![Ticket](/ticket.png)
![Review](/review.png)
![Followers](/followers.png)
