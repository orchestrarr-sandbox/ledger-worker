import os
import socket


def test_the_cache_answers():
    # The ledger keeps its totals in a Redis cache: the pipeline runs one beside the tests
    host = os.environ.get("CACHE_HOST", "localhost")
    with socket.create_connection((host, 6379), timeout=3) as cache:
        cache.sendall(b"PING\r\n")
        assert cache.recv(16).startswith(b"+PONG")
