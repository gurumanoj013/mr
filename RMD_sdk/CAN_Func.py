import os

def CAN_OFF():
    os.popen('sh /home/agx1/Downloads/can_disable.sh')
    print('File Exicuted')

def CAN_ON():
    os.popen('sh /home/agx1/Downloads/can-enable.sh')
    print('File Exicuted')
