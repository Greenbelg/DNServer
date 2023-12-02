import socket, binascii

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("127.0.0.1", 53)
sock.bind(addr)

def getflags(flags_string):
    byte1 = flags_string[0]
    byte2 = flags_string[1]

    QR = "1"

    opcode = "0000"

    AA = "1"

    Tc = "0"

    Rd = "0"

    RA = "0"

    Z = "000"

    Rcode = '0000'

    return int(QR + opcode + AA + Tc + Rd, 2).to_bytes(1, byteorder="big") + int(RA + Z + Rcode,2).to_bytes(1, byteorder="big")

def buildresponse(data):

    tid = "".join(hex(byte)[2:] for byte in data[:2])

    flags = getflags(data[2:4])
    return tid

s, adr = sock.recvfrom(65535)
sock.sendto(b"hello", addr)
print(buildresponse(s))