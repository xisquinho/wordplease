# Wordplease

## Prerequisites

1. Python
2. pip

## Start

Database

```shell
python manage.py migrate
```

Superuser

```shell
python manage.py createsuperuser
```

Running

```shell
python manage.py runserver
```

## Website

http://127.0.0.1:8000

### Users API

- `POST /api/v1/users/

```json
{
  "first_name": "xx",
  "last_name": "xx",
  "username": "xx",
  "email": "xx@xx.com",
  "password": "xx"
}
```

- `GET /api/v1/users/<id>/`
- `PUT /api/v1/users/<id>/`
- `DELETE /api/v1/users/<id>/`

### Blogs API

- `GET /api/v1/blogs/`
- `GET /api/v1/blogs/?ordering=-username&search=loren`

### Posts API

- `GET /api/v1/posts/`
- `GET /api/v1/posts/?ordering=-owner__username`
- `POST /api/v1/posts/`

```json
{
  "username": "admin",
  "first_name": "",
  "last_name": "",
  "num_posts": 0,
  "url": "http://127.0.0.1:8000/blogs/admin/",
  "api_url": "http://127.0.0.1:8000/api/v1/blogs/admin/"
}
```

- `GET /api/v1/posts/<id>/`
- `PUT /api/v1/posts/<id>/`
- `DELETE /api/v1/posts/<id>/`
