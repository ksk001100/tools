import itertools
import socks
import socket
import json
from urllib.request import urlopen
import subprocess
import atexit
import time

class Onion:
    proc = None
    default_socket = socket.socket

    def __init__(self):
        self.start_tor()
        self.set_socks5()
        atexit.register(self.stop_tor)

    def __del__(self):
        self.stop_tor()
        self.remove_socks5()

    def set_socks5(self):
        socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
        socket.socket = socks.socksocket

    def remove_socks5(self):
        socket.socket = self.default_socket

    def start_tor(self):
        self.proc = subprocess.Popen('tor', stdout=subprocess.DEVNULL)
    
    def stop_tor(self):
        self.proc.kill()

    def restart_tor(self):
        self.stop_tor()
        self.start_tor()
        time.sleep(5)


class Client:
    onion = None

    def __init__(self, is_onion=False):
        if is_onion:
            self.onion = Onion()

    def get_global_ip(self):
        res = json.loads(self.get('https://api.ipify.org', {'format': 'json'}))
        return res['ip']

    def get(self, url, params={}):
        q = ''
        if len(params):
            q = '?' + '&'.join(map(lambda x: x[0] + '=' + x[1], params.items()))
        return urlopen(url + q).read().decode('utf8')

    def post(self, url, params={}):
        pass


def generate_passwords(patterns=[]):
    passwords = []
    for n in range(1, len(patterns) + 1):
        for c in itertools.permutations(patterns, n):
            passwords.append(''.join(list(c)))
    return passwords
