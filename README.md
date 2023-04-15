# Users API written with Python and MONGODB

```
git clone

cd <project>

pip3 install -r requirements.txt

python3 app.py
```


# ENV
```dotenv
SECRET_KEY = YOUR_SECRET_KEY
MONGO_URI = YOUR_MONGODB_URL
```


# USING docker
```docker
docker build -t image_name .

docker run -e SECRET_KEY="YOUR_SECRET_KEY" -e MONGO_URI = "YOUR_MONGODB_URL"  image_name:latest


```

# API USUAGE
```docker
○ GET /users - Returns a list of all users.
○ GET /users/<id> - Returns the user with the specified ID.
○ POST /users - Creates a new user with the specified data.
○ PUT /users/<id> - Updates the user with the specified ID with the new data.
○ DELETE /users/<id> - Deletes the user with the specified ID.
```