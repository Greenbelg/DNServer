import binascii
import socket
import dnsquery


def send_udp_message(message, address, port):
    """send_udp_message sends a message to UDP server

    message should be a hexadecimal encoded string
    """
    message = message.replace(" ", "").replace("\n", "")
    server_address = (address, port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(binascii.unhexlify(message), server_address)
        data, _ = sock.recvfrom(4096)
    finally:
        sock.close()
    return binascii.hexlify(data).decode("utf-8")


def format_hex(hex):
    """format_hex returns a pretty version of a hex string"""
    octets = [hex[i:i+2] for i in range(0, len(hex), 2)]
    pairs = [" ".join(octets[i:i+2]) for i in range(0, len(octets), 2)]
    return "\n".join(pairs)

b = dnsquery.dnsquery()
message = b.get_query_for("example.com")

response = send_udp_message(message, "8.8.8.8", 53)
b.a = b.a.replace(" ", "").replace("\n", "")
l = len(bin(int(b.a, 16))[2:].zfill(8))
print(bin(int(response, 16))[2:].zfill(8)[l:][112:]) 
