# API
This is an implementation of a Python web server using Sanic.

## How to Install
Install dependencies:
```
pip install -r requirements.txt
```

## How to Use

- Run:
```
python api.py
```
This will create a local web server with the address of:
```
http://0.0.0.0:8000
```
- Send a POST API request to the endpoint:
```
http://0.0.0.0:8000/login
```
with the following payload:
```
{
"username": "my_username",
"password": "my_password"
}
```
In response you will get a JWT token.
For all other API calls, use this token in the request's *x-access-tokens* header.

## Available Endpoints
- POST http://0.0.0.0:8000/login
- POST http://0.0.0.0:8000/normalize
