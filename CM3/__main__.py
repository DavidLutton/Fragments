import socket
import binascii
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# now connect to the web server on port 80 - the normal http port
s.connect(('192.168.57.200', 6554))
s.send(bytes("lock\x00", 'ascii'))
print(s.recv(200))


s.send(bytes("4", 'ascii'))  # Alive to CM3 device
print(s.recv(6))

s.send(bytes("2", 'ascii'))  # Ask for EPROM state of CM3 device
print(s.recv(136))


s.send(bytes("1\x00", 'ascii'))  # Ask for # of CM3 device
s.send(bytes("1\x00", 'ascii'))  # Ask for # of CM3 device
s.send(bytes("1\x00", 'ascii'))  # Ask for # of CM3 device
s.send(bytes("0\x00", 'ascii'))  # Ask for # ?? # CM3 device

print(s.recv(136))
print(s.recv(136))
print(s.recv(136))
print(s.recv(136))

s.send(bytes("4", 'ascii'))  # Alive to CM3 device
print(s.recv(6))


s.send(bytes("13", 'ascii'))  # Alive to CM3 device
s.send(bytes("0\x00", 'ascii'))  # Alive to CM3 device
print(s.recv(60))
print(s.recv(60))
print(s.recv(60))
print(s.recv(60))

print("Pass")

s.send(bytes("1w", 'ascii'))  # Alive to CM3 device
s.send(bytes("0\x00", 'ascii'))  # Alive to CM3 device
print(s.recv(60))
print(s.recv(60))

s.send(bytes("4", 'ascii'))  # Alive to CM3 device
print(s.recv(6))

print(s.recv(60))
print(s.recv(60))
print(s.recv(60))
print(s.recv(60))

print("Loop")
while [True]:
    s.send(bytes("4", 'ascii'))  # Alive to CM3 device
    s.recv(6)  # recive packet with Alive from CM3 device
    # print()

    a = binascii.hexlify(s.recv(60))
    b = binascii.hexlify(s.recv(60))
    c = binascii.hexlify(s.recv(60))
    d = binascii.hexlify(s.recv(60))
    print(a, b, c, d)
