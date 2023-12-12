# the-eye
Service that collects events data from web applications.

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

### Create Token
```
docker ps
```
Will show you 3 containers, you need to copy the NAME of the IMAGE 'the-eye_app'

```
docker exec -it the-eye_app_NAME bash
python manage.py drf_create_token admin
```
And copy the token returned.

### Access 
```
curl http://127.0.0.1:8000/events/ -H 'Authorization: Token <your_token>'
```
### POST Example
```
curl http://127.0.0.1:8000/events/ -H 'Authorization: Token a9d83a4dbdf9bce9e4ebe15c2d36b71df6e811b2' \
-H "Accept: application/json" \
-H "Content-Type:application/json" \
--data @<(cat <<EOF
{
  "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
  "category": "page interaction",
  "name": "pageview",
  "data": {
    "host": "www.consumeraffairs.com",
    "path": "/"
  },
  "timestamp": "2021-01-01 09:15:27.243860"
}
EOF
)
```
