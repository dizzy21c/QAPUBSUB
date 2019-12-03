import os

qapubsub_ip = os.getenv('QAPUBSUB_IP', '192.168.3.8')
qapubsub_port = os.getenv('QAPUBSUB_PORT', 5672)
qapubsub_user = os.getenv('QAPUBSUB_USER', 'admin')
qapubsub_password = os.getenv('QAPUBSUB_PWD', 'admin')
