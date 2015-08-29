### Setup Instructions
1. git clone `git@github.com:oliviazhang0809/bird.git`
2. Start virtualenv -- `. venv/bin/activate`
3. `pip install` -- this will install dependencies already specified in `requirements.txt` file
4. `python bird.py` -- this will start the server.
5. start redis server

### Example Queries
#### Upsert data into redis
POST `http://127.0.0.1:5000/users`
```json
{
  "id": 1,
  "name": "foo",
  "title": "code hacker"
}
```
* Op successful - StatusCode: 201 CREATED


#### Get data from Redis
GET `http://127.0.0.1:5000/users?/1`

Response object
```json
{
    "title": "code hacker",
    "id": 1,
    "name": "foo"
}
```
* Get successful - StatusCode: 200 OK
* Nothing found - StatusCode: 404 NOTFOUND

#### Delete data
DELETE `http://127.0.0.1:5000/users/1`
* Delete is successful - StatusCode: 200 OK 
* No data to delete - StatusCode: 404 NOTFOUND

#### Erase all data in Redis
POST `http://127.0.0.1:5000/clear`
