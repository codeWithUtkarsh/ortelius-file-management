import requests

API_ENDPOINT = "http://192.168.225.51:5000/file"

#request endpoint
def test_post():
    data = {'compid': 100, 'filetype': 'readme', 'file': open('sample.md', 'rb').read()}
    r = requests.post(url = API_ENDPOINT, data = data)
    print("Status is:%s, Response is:%s  "%(r.status_code,r.text))

test_post()

def test_get():
    r = requests.get(url = API_ENDPOINT, params={'compid': 100, 'filetype': 'readme'})
    print("Status is:%s, Response is:%s  "%(r.status_code,r.text))

# test_get()