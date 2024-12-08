from functools import cached_property
from django.core.cache.backends.redis import (
    RedisCache as _RedisCache,
    RedisCacheClient as _RedisCacheClient
)


class RedisCacheClient(_RedisCacheClient):
    def ttl(self, key: str):
        return self.get_client(key).ttl(key)

    def keys(self, pattern: str = '*'):
        return self.get_client(pattern).keys(pattern)

    def exists(self, key: str):
        return self.get_client(key).exists(key)

    def enqueue(self, queue: str, key: str):
        return self.get_client(key).lpush(queue, key)

    def dequeue(self, queue: str):
        return self.get_client(queue).rpop(queue)


class RedisCache(_RedisCache):
    @cached_property
    def _cache(self):
        return RedisCacheClient(self._servers, **self._options)

    def ttl(self, key: str, version=None):
        return self._cache.ttl(self.make_and_validate_key(key, version=version))

    def keys(self, pattern: str = '*'):
        return self._cache.keys(pattern)

    def exists(self, key: str, version=None):
        return self._cache.exists(self.make_and_validate_key(key, version=version))

    def enqueue(self, queue: str, key: str, version=None):
        return self._cache.enqueue(queue, self.make_and_validate_key(key, version=version))

    def dequeue(self, queue: str):
        return self._cache.dequeue(queue)
