# Redis

## Hands-on

1. start redis server: $redis-server
2. check connection: $redis-cli -h localhost -p 6379 ping

- expected response: PONG

3. connect to server: $redis-cli -h localhost -p 6379

- expected resonse: localhost:6379>

## Tutorial

- [Install Redis on macOS](https://redis.io/docs/getting-started/installation/install-redis-on-mac-os/)
- [Get started](https://redis.io/docs/getting-started/)
- [Redis with Python](https://docs.redis.com/latest/rs/references/client_references/client_python/)

## Package Installation

- $ pip install pip-tools
- $ pip-compile requirements.ini
  - it will generate the requirements.txt with dependency package info in the same directory.
