import itertools
import socks
import socket
import subprocess
import atexit
import time

def set_socks5():
    socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
    socket.socket = socks.socksocket


def generate_passwords(patterns=[]):
    passwords = []
    for n in range(1, len(patterns) + 1):
        for c in itertools.permutations(patterns, n):
            passwords.append(''.join(list(c)))
    return passwords
