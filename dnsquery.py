import binascii

class dnsquery:
    def __init__(self):
        self.query = ""
        self.a = ""

    def get_query_for(self, host):
        self.get_header_for()
        self.get_body_for(host)
        return self.query

    def get_header_for(self):
        self.a += "AA AA 01 00 00 01 00 00 00 00 00 00 "
        self.query += "AA AA 01 00 00 01 00 00 00 00 00 00 "

    def get_body_for(self, host):
        for el in host.split('.'):
            self.query += self.to_hex(len(el)) + " "
            self.query += " ".join(self.to_hex(ord(e)) for e in el)
            self.a += self.to_hex(len(el)) + " "
            self.a += " ".join(self.to_hex(ord(e)) for e in el)
        self.query += "00 00 01 00 01"
        self.a += "00 00 01 00 01"

    def to_hex(self, n):
        return hex(n)[2:] if len(hex(n)) % 2 == 0 else '0' + hex(n)[2:]
    
a = dnsquery()
a.get_query_for(".example.com")
a.a = a.a.replace(" ", "").replace("\n", "")
print(bin(int(a.a, 16))[2:].zfill(8))
print(hex(170)[2:] if len(hex(200)) % 2 == 0 else '0' + hex(256)[2:])
print(binascii.unhexlify(hex(170)[2:] if len(hex(170)) % 2 == 0 else '0' + hex(170)[2:]))
