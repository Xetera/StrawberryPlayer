import logging
import os

ip = os.environ.get('IP_ADDRESS', '127.0.0.1')
FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': ip, 'user': 'Strawberry-Server'}

logger = logging.getLogger('tcpserver')
