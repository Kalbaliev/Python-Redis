
# Redis on Python 

First of All, for using Redis on Python we have to up Redis Server on Docker




## Redis up on Docker

Pull Redis image from [DockerHub](https://hub.docker.com/search?q=redis)
```
docker pull redis
```
Up Redis Server on 6379 port
```
docker run --name redis-server -p 6379:6379 redis
```
## Already everything is okay on Docker side! 
Let's begin Python coding :)



# Python
```python
  pip install redis
```
## Connect to Redis Server on Python
```python
r = redis.Redis(host='localhost', port=6379, db=0)
```
## Pub-Sub (Messaging Broker on Redis) with `pub-sub.py` file

#### Subscribe to channel (channels)
- ***`subscribeChannel (channels)`*** - give channels' names from list type
```python
  python pub-sub.py subscribeChannel ['first-channel','second-channel']
```



#### Publish  message to channel
- ***`publishChannel (channel,msg)`*** - give channel's' name and message from string (***with ***"***(2 quotes)  symbol, not ***'***(1 quote) symbol***)
```python
  python pub-sub.py publishChannel "first-channel" "My first message from Redis"
```
