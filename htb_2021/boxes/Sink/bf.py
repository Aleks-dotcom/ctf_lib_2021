import base64
from hashlib import sha1
import hmac
from time import sleep
b64 = 'AgpH-zpJYaZK0DvQi9-NwwoxT-8'

data = base64.b64decode(b64.encode())

h = ''

for elem in data:
    h += hex(elem)[2:].rjust(2,'0')

print(h)
#h = '0afb9adceae4b42834d4f9b568a71d7eac64426d49'
first_part = 'eyJlbWFpbCI6ImFzZGFzZGFzZEBhIn0.YQPdCw'
test = 'eyJlbWFpbCI6ImFkbWluQHNpbmsuaHRiIiwia2lkIjoiYWFhYWFhYScgVU5JT04gU0VMRUNUICdrZXknOy0tIn0=.YQP4Eg'
hassh = hmac.new(b'key',test.encode(),sha1)
print(base64.b64encode(hassh.digest()).decode())
with open('/usr/share/dirb/wordlists/rockyou.txt','rb') as f:
    line = f.readline()
    while True:
        if line == '':
            continue
        line = f.readline()
        line = line[:-1]
   #     sleep(1)
        hassh = hmac.new(bytes(line),first_part.encode(),sha1).hexdigest()
        if hassh ==h:
            print(f'secret: {str(line)}')
            break
        #else:
           # print(f"{hassh} != {h}")
            #print(f'failed: {str(line)}')





