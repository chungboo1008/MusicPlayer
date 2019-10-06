import socket, signal
import lirc as IR
import RPi.GPIO as GPIO
from  array import array

PORT = 42001
HOST = "localhost"
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Lirc = IR.init("keys")
IR.set_blocking(False, Lirc)    # non-block , will return empty array when no key is pressed

def handler(signal, frame):
    Socket.close()
    GPIO.cleanup()
    exit(0)

signal.signal(signal.SIGTSTP, handler)

def sendCmd(cmd):
    n = len(cmd)
    a = array('c')
    a.append(chr((n >> 24) & 0xFF))
    a.append(chr((n >> 16) & 0xFF))
    a.append(chr((n >> 8) & 0xFF))
    a.append(chr(n & 0xFF))
    Socket.send(a.tostring() + cmd)
