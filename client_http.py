import requests

r = requests.get("http://127.0.0.1:8080/", params={"name":'john'})
print("Request method: GET, \
    Response status_code: {}, Response data: {}".format(r.status_code, r.text))
r = requests.post("http://127.0.0.1:8080/", params = {'name':'andrei', 'last_name':'ionescu'})
print("Request method: POST, \
    Response status_code: {}, Response data: {}".format(r.status_code, r.text))
r = requests.delete("http://127.0.0.1:8080/", params={'name':'lee', 'last_name':'jones'})
print("Request method: DELETE, \
    Response status_code: {}, Response data: {}".format(r.status_code, r.text))



