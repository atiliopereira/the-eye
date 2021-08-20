# the-eye
Service that collect events data from web applications.

## Requirements

- Python 3.8+
- PostgreSQL 12+
- Rabbitmq 3.9+


## Install using docker-compose

```
git clone https://github.com/atiliopereira/the-eye.git && cd the-eye
docker-compose up
```

## Test / Use
It is assumed that the event categories (model Category instances) exist, but the possibility of creating them has been added 
through http://127.0.0.1/:8000/admin/events/category/ with the credentials:
```
us: admin
pw: admin
```
It is also assumed that the creation of the sessions and their ids (session_id) are managed by the application.

To test an Event POST you can do it through the Django-rest-framework interface from:
http://127.0.0.1/:8000/events/
