import datetime

from sanic import Sanic, json
import jwt

USER_NAME = "my_username"
USER_PASSWORD = "my_password"
SECRET_KEY = "cf487ba38a2154b42a8ef8d96a47171b"

app = Sanic("varonis_task_app")


def validate_token(request):
    is_token_valid = False
    token = None

    if 'x-access-tokens' in request.headers:
        token = request.headers['x-access-tokens']

    if not token:
        return False

    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        is_token_valid = data["public_id"] == USER_NAME
    except Exception as e:
        print(e)

    return is_token_valid


@app.route('/login', methods=['POST'])
def login(request):
    payload = request.json

    if not ("username" in payload and "password" in payload):
        return json({"error": "missing user name or password"}, status=401)

    if payload["username"] == USER_NAME and payload["password"] == USER_PASSWORD:
        token = jwt.encode(
            {'public_id': payload["username"], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45)},
            SECRET_KEY, "HS256")
        return json({'token': token})

    return json({"error": "wrong username or password"}, status=401)


@app.route('/normalize', methods=['POST'])
def normalize(request):
    if validate_token(request):
        payload = request.json
        return json({d["name"]: v for d in payload for k, v in d.items() if "val" in k.lower()})

    else:
        return json({"error": "invalid or missing token"}, status=401)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
